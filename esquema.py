from PIL import Image
import matplotlib.pyplot as plt
import random
import numpy as np
import urllib.request

def fuente(url):
    urllib.request.urlretrieve(url, 'imagen.jpg')
    return Image.open('imagen.jpg')

def transmisor(imagen):
    return imagen.convert("L")

def canal_receptor(imagen_gris, probabilidad_error):
    img_width, img_height = imagen_gris.size
    received_symbols = []

    for pixel_value in np.array(imagen_gris).flatten():
        if random.random() < probabilidad_error:
            # Introducir un error (cambiar el valor del píxel)
            received_symbols.append(random.randint(0, 255))
        else:
            received_symbols.append(pixel_value)

    return np.array(received_symbols, dtype=np.uint8).reshape((img_height, img_width))

def destino(original, con_ruido):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(np.array(original), cmap='gray')
    plt.title('Imagen Original')

    plt.subplot(1, 2, 2)
    plt.imshow(np.array(con_ruido), cmap='gray')
    plt.title('Imagen con Ruido')

    plt.tight_layout()
    plt.show()

# Cargar la imagen original
url_imagen = r'https://www.lavozdelafrontera.com.mx/cultura/d8l25j-luisito-comunica-sonic.jpg/alternates/LANDSCAPE_768/Luisito%20comunica%20sonic.jpg'
imagen_original = fuente(url_imagen)

# Convertir la imagen a escala de grises
imagen_gris = transmisor(imagen_original)

# Simular el canal con ruido
probabilidad_error = 0.1  # Probabilidad de error del canal
imagen_con_ruido = canal_receptor(imagen_gris, probabilidad_error)

# Mostrar las imágenes
destino(imagen_gris, imagen_con_ruido)
