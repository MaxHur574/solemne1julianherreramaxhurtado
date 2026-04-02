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
   ```

3. Instalar las dependencias:

   ```
   uv sync
   ```

---

## ▶️ Ejecutar la aplicación localmente

Con el entorno virtual activado, ejecuta el siguiente comando desde la raíz del proyecto:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

La aplicación estará disponible en: `http://localhost:8000/time`

> La flag `--reload` recarga automáticamente el servidor al detectar cambios en el código. Se recomienda solo en desarrollo.

---

## 🐳 Ejecutar con Docker

### 1. Construir la imagen

```bash
docker build -t fastapi-hora-chile .
```

### 2. Ejecutar el contenedor

```bash
docker run -d -p 8000:8000 fastapi-hora-chile
```

La aplicación estará disponible en: `http://localhost:8000/time`

### Detener el contenedor

```bash
docker ps                        # obtener el CONTAINER ID
docker stop <CONTAINER_ID>
```

---

## 🧪 Testear el API

### Con el navegador

Abre tu navegador y visita:

```
http://localhost:8000/time
```

También puedes acceder a la documentación interactiva automática de FastAPI:

```
http://localhost:8000/docs
```

### Con curl

```bash
curl http://localhost:8000/time
```

Respuesta esperada (ejemplo):

```json
{
  "hora_chile": "2025-04-02T15:30:00-04:00"
}
```

---

## 🧾 Estructura del proyecto

```
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── main.py
├── test_main.py
├── Dockerfile
├── .dockerignore
├── .gitignore
├── pyproject.toml
└── README.md
```

