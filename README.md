# Convertidor de Imágenes a WebP

Este script convierte imágenes en un directorio a formato WebP sin pérdida de calidad y las guarda en una subcarpeta `webp`.

## Requisitos

- Python 3.x
- pip (el gestor de paquetes de Python)

## Instalación

1. Clona este repositorio o descarga los archivos `convert_to_webp.py` y `requirements.txt`.

2. Navega al directorio donde se encuentran los archivos y ejecuta el siguiente comando para instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Asegúrate de tener tus imágenes en un directorio específico.

2. Modifica el script `convert_to_webp.py` para que el `input_directory` apunte al directorio que contiene tus imágenes:

   ```python
   if __name__ == "__main__":
       # Directorio de ejemplo que contiene las imágenes a convertir
       # Actualmente ./images/
       input_directory = "./images/"

       # Llama a la función para convertir y comprimir las imágenes
       compress_images_to_webp(input_directory)
   ```

3. Ejecuta el script:

   ```bash
   python convert_to_webp.py
   ```

   o

   ```bash
   py convert_to_webp.py

   ```

4. Las imágenes convertidas se guardarán en una subcarpeta llamada `webp` dentro del directorio que especificaste.

## Notas

- Este script convierte todas las imágenes en el directorio especificado a formato WebP sin pérdida de calidad.
- Asegúrate de que el directorio de salida tenga permisos de escritura.

## Contribuir

Si deseas contribuir a este proyecto, por favor, realiza un fork del repositorio y envía un pull request con tus cambios.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.
