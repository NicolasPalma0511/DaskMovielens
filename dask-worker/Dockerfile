# Dockerfile para los workers de Dask
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

# Exponer los puertos de los workers
EXPOSE 8786

# Copiar script de inicio del worker
COPY start_worker.sh /app/

# Ejecutar el worker
CMD ["bash", "/app/start_worker.sh"]
