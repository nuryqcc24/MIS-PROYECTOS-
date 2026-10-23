// Prueba del buzzer: suena 1 segundo, calla 1 segundo, para siempre.
// Buzzer: cable rojo -> G25 (fila 20, columna a); cable negro -> línea azul (GND)

const int BUZZER = 25;

void setup() {
  pinMode(BUZZER, OUTPUT);
}

void loop() {
  digitalWrite(BUZZER, HIGH);
  delay(1000);
  digitalWrite(BUZZER, LOW);
  delay(1000);
}
