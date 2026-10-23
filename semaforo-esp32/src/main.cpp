// Semáforo peatonal con sonido - ESP32
// Paso 4: semáforo + buzzer para peatones
//
// Conexión (patas cortas de todos los LEDs -> línea azul del riel = GND):
//   G13 (fila 26) -> resistencia -> pata larga LED amarillo
//   G27 (fila 22) -> jumper -> resistencia -> pata larga LED verde
//   G26 (fila 21) -> jumper -> resistencia -> pata larga LED rojo
//   G25 (fila 20) -> cable rojo del buzzer; cable negro -> línea azul
//
// El semáforo es el de los autos. Cuando está en ROJO cruzan los peatones,
// y el buzzer los avisa: bip lento = pueden cruzar, bip rápido = apúrense.

#include <Arduino.h>  // instrucciones de Arduino: digitalWrite, delay, HIGH, LOW...

// ===== TIEMPOS (en segundos): cámbialos aquí =====
const float TIEMPO_ROJO = 25;     // los peatones cruzan
const float TIEMPO_VERDE = 30;     // incluye el parpadeo del final
const float TIEMPO_AMARILLO = 3;
const int PARPADEOS_VERDE = 5;     // veces que parpadea antes de cambiar
const float AVISO_RAPIDO = 5;      // últimos segundos del rojo con bip rápido
// =================================================

const int LED_ROJO = 26;
const int LED_AMARILLO = 13;
const int LED_VERDE = 27;
const int BUZZER = 25;

void apagarTodos() {
  digitalWrite(LED_ROJO, LOW);
  digitalWrite(LED_AMARILLO, LOW);
  digitalWrite(LED_VERDE, LOW);
  digitalWrite(BUZZER, LOW);
}

void esperar(float segundos) {
  delay(segundos * 1000);
}

// Hace "bip" durante el tiempo indicado: sonido y silencio en segundos
void pitar(float segundos, float sonido, float silencio) {
  int veces = segundos / (sonido + silencio);
  for (int i = 0; i < veces; i++) {
    digitalWrite(BUZZER, HIGH);
    esperar(sonido);
    digitalWrite(BUZZER, LOW);
    esperar(silencio);
  }
}

// Mensajes por USB para el dashboard (ver carpeta dashboard):
//   FASE,<nombre>,<segundos>  -> empieza una fase del semáforo y cuánto dura
//   LUZ,<color>               -> qué LED está prendido en este momento
void avisarFase(const char* nombre, float segundos) {
  Serial.printf("FASE,%s,%.1f\n", nombre, segundos);
}

void prender(int pin, const char* color) {
  apagarTodos();
  if (pin >= 0) digitalWrite(pin, HIGH);
  Serial.printf("LUZ,%s\n", color);
}

void setup() {
  Serial.begin(115200);
  pinMode(LED_ROJO, OUTPUT);
  pinMode(LED_AMARILLO, OUTPUT);
  pinMode(LED_VERDE, OUTPUT);
  pinMode(BUZZER, OUTPUT);
}

void loop() {
  // Verde: pasan los autos, los peatones esperan (silencio)
  avisarFase("VERDE", TIEMPO_VERDE);
  prender(LED_VERDE, "VERDE");
  esperar(TIEMPO_VERDE - PARPADEOS_VERDE * 0.6);

  // Verde parpadeando: ya va a cambiar
  for (int i = 0; i < PARPADEOS_VERDE; i++) {
    prender(-1, "APAGADO");
    esperar(0.3);
    prender(LED_VERDE, "VERDE");
    esperar(0.3);
  }

  // Amarillo: precaución (silencio)
  avisarFase("AMARILLO", TIEMPO_AMARILLO);
  prender(LED_AMARILLO, "AMARILLO");
  esperar(TIEMPO_AMARILLO);

  // Rojo: paran los autos y cruzan los peatones
  avisarFase("ROJO", TIEMPO_ROJO);
  prender(LED_ROJO, "ROJO");
  pitar(TIEMPO_ROJO - AVISO_RAPIDO, 0.15, 0.85);  // bip... bip... (pueden cruzar)
  pitar(AVISO_RAPIDO, 0.1, 0.1);                  // bipbipbip (apúrense)
}
