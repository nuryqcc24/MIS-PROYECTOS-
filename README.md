# 🚦 Portafolio de Proyectos & Control Web

<p align="center">
  <img src="https://img.shields.io/badge/Status-En%20Desarrollo-success?style=for-the-badge&logo=git" alt="Status" />
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License" />
  <img src="https://img.shields.io/badge/Hardware-Serial%20%2F%20COM-orange?style=for-the-badge&logo=arduino" alt="Hardware" />
</p>

> Espacio dedicado a la recopilación, desarrollo y despliegue de proyectos interactivos, interfaces de automatización y aplicaciones web.

---

## 📌 Proyecto Destacado: Sistema de Control de Semáforo Inteligente

Panel web interactivo diseñado para la monitorización en tiempo real del ciclo semafórico, control peatonal y sincronización de estados vía comunicación serial.

👉 **[Ver el proyecto: código, conexiones y cómo usarlo](semaforo-esp32/)**

### 🛠️ Características Principales
* ⏱️ **Monitoreo de Ciclos:** Visualización dinámica de fases activa (Verde, Amarillo, Rojo) con temporizador en tiempo real.
* 🚶 **Señalización Peatonal:** Alertas visuales sincronizadas para flujo de peatones.
* 🔌 **Conectividad:** Enlace directo de comunicación serial (`COM3`) con microcontrolador.
* 📋 **Registro de Eventos:** Historial cronológico de cambios de estado y transiciones.

---

## 💻 Tecnologías Utilizadas

| Categoría | Tecnologías / Herramientas |
| :--- | :--- |
| **Frontend** | HTML5, CSS3 Moderno, JavaScript |
| **Hardware / Comunicación** | Puerto Serie (COM), Controladores de E/S |
| **Control de Versiones** | Git & GitHub |

---

## 📂 Estructura del Repositorio

```text
├── semaforo-esp32/       # Sistema de Control de Semáforo Inteligente
│   ├── src/main.cpp      # Programa del ESP32 (LEDs, buzzer y mensajes por serial)
│   ├── platformio.ini    # Configuración de PlatformIO
│   ├── dashboard/        # Panel web en tiempo real (Python + HTML)
│   ├── PRUEBA_BUZZER/    # Sketch de prueba del buzzer
│   └── README.md         # Documentación del proyecto
└── README.md             # Este portafolio
