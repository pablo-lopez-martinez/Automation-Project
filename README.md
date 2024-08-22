# Automatización de Facturas

Este proyecto de Python automatiza la generación de facturas a partir de un archivo Excel. Utiliza `cotizaciones.xlsx` como archivo de entrada para leer las cotizaciones y generar facturas en formato PDF, que se guardan en el directorio `facturas`. El proyecto incluye también el logo de la compañía y funciones auxiliares para facilitar la creación de facturas.

## Estructura del Repositorio

El repositorio contiene los siguientes archivos y directorios:

- `cotizaciones.xlsx`: Archivo de entrada con las cotizaciones que se convertirán en facturas.
- `facturas/`: Directorio donde se guardan las facturas generadas.
- `logo.jpg`: Logo de la compañía, incluido en las facturas.
- `functions.py`: Archivo con funciones auxiliares para el procesamiento y la creación de facturas.
- `script.py`: Archivo principal que ejecuta el proceso de conversión de cotizaciones a facturas.

## Dependencias

Para ejecutar este proyecto, necesitarás las siguientes bibliotecas de Python:

- `pandas`: Para el manejo de datos en el archivo Excel.
- `reportlab`: Para la creación de archivos PDF.

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone <URL_DEL_REPOSITORIO>

2. **Runnea el script:**

   ```bash
   python script.py
