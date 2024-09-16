# Usar una imagen base de Python 3.9 slim
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /usr/src/app

# Instalar dependencias de sistema necesarias para pyodbc y SQL Server ODBC drivers
RUN apt-get update && \
    apt-get install -y gcc g++ unixodbc-dev curl gnupg2 && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Copiar el archivo de requerimientos al contenedor
COPY requirements.txt .

# Instalar las dependencias desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos de la aplicación al contenedor
COPY . .

# Exponer el puerto (si es necesario)
EXPOSE 8787

# Ejecutar el script Python por defecto
CMD ["python", "process_data.py"]
