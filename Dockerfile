# Imagen base ligera de Python
FROM python:3.11-slim

# Setear directorio de trabajo
WORKDIR /app

# Copiar dependencias y instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la API
COPY ./app ./app

# Copiar el modelo dentro del contenedor
COPY ./models ./app/models

# Copiar archivo de variables de entorno
COPY .env .env

# Exponer puerto de la API
EXPOSE 8000

# Comando para levantar la API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
