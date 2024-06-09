from PIL import Image
import os

def convert_to_webp(input_path, output_path):
    img = Image.open(input_path)
    img.save(output_path, format='webp', lossless=False)
    print(f"Imagen convertida y guardada en {output_path}")

def compress_images_to_webp(directory):
    webp_directory = os.path.join(directory, "webp")
    if not os.path.exists(webp_directory):
        os.makedirs(webp_directory)

    for filename in os.listdir(directory):
        input_path = os.path.join(directory, filename)
        if os.path.isfile(input_path) and not filename.endswith('.webp'):
            output_path = os.path.join(webp_directory, f"{os.path.splitext(filename)[0]}.webp")
            convert_to_webp(input_path, output_path)
            print(f"{filename} convertido a {output_path}")

if __name__ == "__main__":
    # Directorio de ejemplo que contiene las imágenes a convertir
    # Actualmente ./images/
    input_directory = "./images/"

    # Llama a la función para convertir y comprimir las imágenes
    compress_images_to_webp(input_directory)
