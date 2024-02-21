
import cv2
import pytesseract
import numpy as np
import re

def ocr_white_part(imagen, config, umbral_inv):
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('gris', gris)
    #cv2.waitKey(0)
    
    # Decidir si usar umbralización inversa o normal
    if umbral_inv:
        _, umbral = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    else:
        _, umbral = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    #cv2.imshow('umbral', umbral)
    #cv2.waitKey(0)
    
    # Dilatar el texto para cerrar huecos dentro de los caracteres
    kernel = np.ones((1, 1), np.uint8)
    dilatacion = cv2.dilate(umbral, kernel, iterations=1)
    #cv2.imshow('dilatacion', dilatacion)
    #cv2.waitKey(0)
    
    # Erosionar para deshacer la dilatación excesiva
    erosion = cv2.erode(dilatacion, kernel, iterations=1)
    #cv2.imshow('Erosion', erosion)
    #cv2.waitKey(0)
    
    # Extraer el texto con pytesseract
    texto = pytesseract.image_to_string(erosion, config=config.PYTESSERACT_CONFIG)
    texto_limpio = re.sub(r'\W+', ' ', texto)
    return texto_limpio
