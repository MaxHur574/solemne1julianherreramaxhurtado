# Imagen base oficial de Python
FROM python:3.13-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY . .

# Instalar dependencias necesarias
RUN pip install --no-cache-dir fastapi uvicorn ntplib tzdata

# Exponer el puerto donde correrá la app
EXPOSE 8000

# Comando para ejecutar el servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
