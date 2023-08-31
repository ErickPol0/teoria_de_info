import numpy as np
import base64
from PIL import Image
import io
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from random import randint
from random import randrange
import urllib.request

def fuente(ruta):  
    urllib.request.urlretrieve(ruta,'gfg.jpg')
    return Image.open("gfg.jpg")

def transmisor(img):
    im_file = BytesIO()
    img.save(im_file, format="JPEG")
    im_bytes = im_file.getvalue() 
    return base64.b64encode(im_bytes)

def canal(cod):
    im_bytes = base64.b64decode(cod)  
    im_file = BytesIO(im_bytes)  
    img = Image.open(im_file)  

    width, height = img.size
    img2 = Image.new("RGB", (width, height))

    pixel_values = list(img.getdata())
    for x in range(width) :
        for y in range(height) :
            ra = randrange(5)
            rb = randrange(5)
            if ra == rb:
                r = randint(0,25)
                g = randint(0,255)
                b = randint(0,255)
                img2.putpixel((x,y), (r, g, b))
            else:
                r = pixel_values[width*y+x][0]
                g = pixel_values[width*y+x][1]
                b = pixel_values[width*y+x][2]
                img2.putpixel((x,y), (r, g, b))

    im_file = BytesIO()
    img2.save(im_file, format="JPEG")
    im_bytes = im_file.getvalue()  
    return base64.b64encode(im_bytes)

def receptor(cod):
    im_bytes = base64.b64decode(cod)   
    im_file = BytesIO(im_bytes)  
    return Image.open(im_file) 

def destino(img_dec):
    img_dec.show()

img = fuente(r'https://www.lavozdelafrontera.com.mx/cultura/d8l25j-luisito-comunica-sonic.jpg/alternates/LANDSCAPE_768/Luisito%20comunica%20sonic.jpg')
img_cod = transmisor(img)
img_cod = canal(img_cod)
img_dec = receptor(img_cod)
destino(img_dec)
