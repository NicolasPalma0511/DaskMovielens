# Dockerfile para el contenedor de procesamiento
FROM python:3.9-slim

# Instalar dependencias
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# Copiar el archivo de dependencias
COPY requirements.txt .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la aplicación
COPY app/ /app/

# Exponer el puerto (si es necesario)
EXPOSE 8787

# Comando de inicio
CMD ["python", "process_data.py"]
