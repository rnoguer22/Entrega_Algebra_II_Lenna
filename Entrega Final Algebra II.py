import numpy as np
import imageio

NOMBRE_IMAGEN = "lenna.jpg"

def leer_imagen(ruta):
    return np.array(imageio.imread(ruta), dtype='int').tolist()


def guardar_imagen(ruta, matriz):
    return imageio.imwrite(ruta, np.array(matriz, dtype="uint8"))



def filtro_1(nombre_imagen, filtro: str):

    def comprobacion(i):
        if pixel_nuevo[i] < 0:
            pixel_nuevo[i] = 0
        elif pixel_nuevo[i] > 255:
            pixel_nuevo[i] = 255
        else:
            pass

    matriz = leer_imagen(nombre_imagen)

    if filtro == "sepia":
        M = np.array([
            [0.393, 0.769, 0.189],
            [0.349, 0.686, 0.168],
            [0.272, 0.534, 0.131]
            ])

    if filtro == "gris":
        M = np.array([
            [1/3, 1/3, 1/3],
            [1/3, 1/3, 1/3],
            [1/3, 1/3, 1/3]
            ])        

    ancho = len(matriz[0])
    alto = len(matriz)

    for y in range(alto):
        for x in range(ancho):

            pixel = matriz[y][x]
            pixel_nuevo = np.dot(M, np.array(pixel))

            for i in range(len(pixel_nuevo)):
                round(pixel_nuevo[i])
                comprobacion(i)

            matriz[y][x] = pixel_nuevo
    return matriz



def negativo(nombre_imagen):

    def comprobacion(i):
        if pixel_nuevo[i] < 0:
            pixel_nuevo[i] = 0
        elif pixel_nuevo[i] > 255:
            pixel_nuevo[i] = 255
        else:
            pass

    matriz = leer_imagen(nombre_imagen)

    M = np.array([
        [-1, 0, 0],
        [0, -1, 0],
        [0, 0, -1]
        ])
    
    V = np.array([255, 255, 255])
       
    ancho = len(matriz[0])
    alto = len(matriz)

    for y in range(alto):
        for x in range(ancho):

            pixel = matriz[y][x]
            pixel_nuevo = np.add(np.dot(M, np.array(pixel)), V)

            for i in range(len(pixel_nuevo)):
                round(pixel_nuevo[i])
                comprobacion(i)

            matriz[y][x] = pixel_nuevo
    return matriz



def filtro_2(nombre_imagen, filtro: str, ajuste: int):

    def comprobacion(i):
        if pixel_nuevo[i] < 0:
            pixel_nuevo[i] = 0
        elif pixel_nuevo[i] > 255:
            pixel_nuevo[i] = 255
        else:
            pass

    matriz = leer_imagen(nombre_imagen)

    if filtro == "rojo":
        M = ([ajuste, 0, 0])

    elif filtro == "verde":
        M = ([0, ajuste, 0])

    elif filtro == "azul":
        M = ([0, 0, ajuste])

    elif filtro == "brillo":
        M = ([ajuste, ajuste, ajuste])  

    ancho = len(matriz[0])
    alto = len(matriz)

    for y in range(alto):
        for x in range(ancho):

            pixel = matriz[y][x]
            pixel_nuevo = np.add(M, np.array(pixel))

            for i in range(len(pixel_nuevo)):
                round(pixel_nuevo[i])
                comprobacion(i)

            matriz[y][x] = pixel_nuevo
    return matriz


guardar_imagen("Lenna_sepia.png", filtro_1(NOMBRE_IMAGEN, "sepia"))
guardar_imagen("Lenna_gris.png", filtro_1(NOMBRE_IMAGEN, "gris"))
guardar_imagen("Lenna_negativo.png", negativo(NOMBRE_IMAGEN))
guardar_imagen("Lenna_rojo.png", filtro_2(NOMBRE_IMAGEN, "rojo", 50))
guardar_imagen("Lenna_verde.png", filtro_2(NOMBRE_IMAGEN, "verde", 125))
guardar_imagen("Lenna_azul.png", filtro_2(NOMBRE_IMAGEN, "azul", 150))
guardar_imagen("Lenna_brillo.png", filtro_2(NOMBRE_IMAGEN, "brillo", 100))