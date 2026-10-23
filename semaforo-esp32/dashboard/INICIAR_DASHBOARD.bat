@echo off
rem Abre el dashboard del semáforo en el navegador.
rem Ciérralo (Ctrl+C o cerrando esta ventana) antes de subir un programa nuevo al ESP32.
cd /d "%~dp0"
if not exist .venv (
  echo Preparando Python por primera vez...
  py -3 -m venv .venv || python -m venv .venv
  .venv\Scripts\python -m pip install pyserial
)
.venv\Scripts\python servidor.py
pause
