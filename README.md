# <img src="assets/iconos/semaforo.svg" width="34" /> Portafolio de Proyectos & Control Web

<p align="center">
  <img src="https://img.shields.io/badge/Status-En%20Desarrollo-success?style=for-the-badge&logo=git" alt="Status" />
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License" />
  <img src="https://img.shields.io/badge/Hardware-Serial%20%2F%20COM-orange?style=for-the-badge&logo=arduino" alt="Hardware" />
</p>

> Espacio dedicado a la recopilación, desarrollo y despliegue de proyectos interactivos, interfaces de automatización y aplicaciones web.

---

## <img src="assets/iconos/pin.svg" width="28" /> Proyecto Destacado: Sistema de Control de Semáforo Inteligente

Panel web interactivo diseñado para la monitorización en tiempo real del ciclo semafórico, control peatonal y sincronización de estados vía comunicación serial.

<p align="center">
  <img src="semaforo-esp32/fotos/semaforo-amarillo.webp" alt="Semáforo en amarillo" width="40%" />
  &nbsp;
  <img src="semaforo-esp32/fotos/semaforo-verde.webp" alt="Semáforo en verde" width="40%" />
</p>

<img src="assets/iconos/flecha.svg" width="18" /> **[Ver el proyecto: código, conexiones y cómo usarlo](semaforo-esp32/)**

### <img src="assets/iconos/herramienta.svg" width="22" /> Características Principales
* <img src="assets/iconos/reloj.svg" width="18" /> **Monitoreo de Ciclos:** Visualización dinámica de fases activa (Verde, Amarillo, Rojo) con temporizador en tiempo real.
* <img src="assets/iconos/peaton.svg" width="18" /> **Señalización Peatonal:** Alertas visuales sincronizadas para flujo de peatones.
* <img src="assets/iconos/enchufe.svg" width="18" /> **Conectividad:** Enlace directo de comunicación serial (`COM3`) con microcontrolador.
* <img src="assets/iconos/lista.svg" width="18" /> **Registro de Eventos:** Historial cronológico de cambios de estado y transiciones.

---

## <img src="assets/iconos/laptop.svg" width="28" /> Tecnologías Utilizadas

| Categoría | Tecnologías / Herramientas |
| :--- | :--- |
| **Frontend** | HTML5, CSS3 Moderno, JavaScript |
| **Hardware / Comunicación** | Puerto Serie (COM), Controladores de E/S |
| **Control de Versiones** | Git & GitHub |

---

## <img src="assets/iconos/carpeta.svg" width="28" /> Estructura del Repositorio

```text
├── semaforo-esp32/       # Sistema de Control de Semáforo Inteligente
│   ├── src/main.cpp      # Programa del ESP32 (LEDs, buzzer y mensajes por serial)
│   ├── platformio.ini    # Configuración de PlatformIO
│   ├── dashboard/        # Panel web en tiempo real (Python + HTML)
│   ├── PRUEBA_BUZZER/    # Sketch de prueba del buzzer
│   └── README.md         # Documentación del proyecto
├── assets/iconos/        # Íconos del README
└── README.md             # Este portafolio
