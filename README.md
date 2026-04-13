# PracticaGitHubCopilot

Proyecto de práctica para aprender GitHub Copilot y automatización con Python y Selenium.

## Descripción

Este repositorio contiene ejemplos educativos de:
- Operaciones matemáticas básicas en Python
- Automatización de navegador con Selenium WebDriver
- Containerización con Docker

## Requisitos

- Python 3.12+
- pip
- Docker (opcional)
- Google Chrome + ChromeDriver (para las pruebas de Selenium)

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

### Ejecutar localmente

```bash
# Operaciones matemáticas básicas
python testPython.py

# Saludo según la hora del día y suma de números
python aprendizajePocasEtapas.py

# Pruebas de automatización web con Selenium
python selenium_saucedemo_test.py
```

### Ejecutar con Docker

```bash
docker build -t practica-copilot .
docker run practica-copilot
```

## Estructura del proyecto

- `testPython.py` — Operaciones matemáticas básicas con type hints y docstrings
- `aprendizajePocasEtapas.py` — Saludo según la hora actual y suma de dos números
- `selenium_saucedemo_test.py` — Pruebas de automatización web en saucedemo.com
- `Dockerfile` — Configuración para ejecutar el proyecto en un contenedor
- `.dockerignore` — Archivos excluidos del contexto de Docker
