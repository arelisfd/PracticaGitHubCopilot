FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VIRTUAL_ENV=/opt/venv

WORKDIR /app

# Crear el entorno virtual dentro del contenedor
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Copiar el proyecto
COPY . /app

# Instalar dependencias si existe requirements.txt
RUN pip install --upgrade pip && \
    if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Ejecutar la aplicación principal
CMD ["python", "aprendizajePocasEtapas.py"]
