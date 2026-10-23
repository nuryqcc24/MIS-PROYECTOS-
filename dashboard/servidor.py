"""Dashboard del semáforo: lee el ESP32 por USB y muestra en el navegador
qué luz está encendida en tiempo real.

Uso:  INICIAR_DASHBOARD.bat   (o: .venv\\Scripts\\python servidor.py)
Luego abre http://127.0.0.1:8001 en el navegador.

Mientras el dashboard está abierto ocupa el puerto COM3: ciérralo antes de
subir un programa nuevo al ESP32.
"""

import json
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import serial
from serial.tools import list_ports

PUERTO = None  # None = detectar el ESP32 solo; o fijarlo, por ejemplo "COM3"
BAUDIOS = 115200
DIRECCION = ("127.0.0.1", 8001)
PAGINA = Path(__file__).with_name("index.html")


def detectar_puerto():
    """Busca el ESP32 entre los puertos serie por su chip USB (CP210x o CH340)."""
    for p in list_ports.comports():
        texto = f"{p.description} {p.manufacturer or ''}".lower()
        if any(chip in texto for chip in ("cp210", "ch340", "usb serial", "uart")):
            return p.device
    return None


class Semaforo:
    """Guarda el último estado que mandó el ESP32."""

    def __init__(self):
        self.lock = threading.Lock()
        self.conectado = False
        self.mensaje = "Iniciando"
        self.luz = "APAGADO"
        self.fase = None
        self.duracion = 0.0
        self.inicio_fase = time.time()
        self.ciclos = 0
        self.historial = []  # últimas fases: [hora, fase]
        threading.Thread(target=self._leer, daemon=True).start()

    def _procesar(self, linea):
        partes = linea.split(",")
        with self.lock:
            if partes[0] == "LUZ" and len(partes) == 2:
                self.luz = partes[1]
            elif partes[0] == "FASE" and len(partes) == 3:
                try:
                    self.duracion = float(partes[2])
                except ValueError:
                    return
                self.fase = partes[1]
                self.inicio_fase = time.time()
                if self.fase == "VERDE":
                    self.ciclos += 1
                self.historial = ([[time.strftime("%H:%M:%S"), self.fase]] + self.historial)[:8]

    def _leer(self):
        while True:
            try:
                puerto = PUERTO or detectar_puerto()
                if puerto is None:
                    raise serial.SerialException("ESP32 no encontrado")
                s = serial.Serial()
                s.port, s.baudrate, s.timeout = puerto, BAUDIOS, 1
                s.dtr = s.rts = False  # evita reiniciar el ESP32 al abrir el puerto
                s.open()
                s.reset_input_buffer()  # descarta mensajes viejos acumulados
                with s:
                    self.conectado, self.mensaje = True, f"Conectado a {puerto}"
                    while True:
                        linea = s.readline().decode(errors="ignore").strip()
                        if linea:
                            self._procesar(linea)
            except serial.SerialException as e:
                texto = str(e).lower()
                self.conectado = False
                self.mensaje = ("Puerto ocupado (¿Arduino IDE o PlatformIO abierto?)"
                                if "denied" in texto or "acceso" in texto
                                else "ESP32 desconectado")
                time.sleep(2)  # reintenta solo

    def estado(self):
        with self.lock:
            transcurrido = time.time() - self.inicio_fase
            return {
                "conectado": self.conectado,
                "mensaje": self.mensaje,
                "luz": self.luz,
                "fase": self.fase,
                "duracion": self.duracion,
                "restante": max(0.0, self.duracion - transcurrido),
                "ciclos": self.ciclos,
                "historial": self.historial,
            }


semaforo = Semaforo()


class Manejador(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/estado":
            cuerpo = json.dumps(semaforo.estado()).encode()
            tipo = "application/json"
        elif self.path in ("/", "/index.html"):
            cuerpo = PAGINA.read_bytes()
            tipo = "text/html; charset=utf-8"
        else:
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", tipo)
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(cuerpo)

    def log_message(self, *args):
        pass  # no llenar la consola con cada consulta


if __name__ == "__main__":
    url = f"http://{DIRECCION[0]}:{DIRECCION[1]}"
    print(f"Dashboard del semáforo en {url}  (Ctrl+C para cerrar)")
    threading.Timer(1, webbrowser.open, [url]).start()
    ThreadingHTTPServer(DIRECCION, Manejador).serve_forever()
