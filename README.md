# Proyecto FastAPI - Hora Oficial de Chile

Este proyecto expone un endpoint en **FastAPI** que devuelve la hora oficial de Chile (zona horaria `America/Santiago`) obtenida desde un servidor NTP.

---
![CI](https://github.com/MaxHur574/solemne1julianherreramaxhurtado/actions/workflows/ci.yml/badge.svg)

## 🚀 Requisitos

- Python 3.13
- Entorno virtual (`venv`)
- Dependencias:
  - fastapi
  - uvicorn
  - pytest
  - ntplib
  - tzdata

---

## ⚙️ Instalación

1. Clonar o descargar el repositorio.
2. Crear y activar el entorno virtual:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\activate.bat
