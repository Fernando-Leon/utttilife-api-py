
import cv2
import pytesseract
import numpy as np
import re

def ocr_black_part(imagen, config):
    # Convertir a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('gris', gris)
    #cv2.waitKey(0)
    # Aplicar umbralización adaptativa para mejorar el contraste del texto
    umbral = cv2.adaptiveThreshold(gris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY, 11, 2)
    #cv2.imshow('umbral', umbral)
    #cv2.waitKey(0)
    # Invertir la imagen para que el texto sea blanco y el fondo negro
    umbral_invertido = cv2.bitwise_not(umbral)
    #cv2.imshow('umbral_invertido', umbral)
    #cv2.waitKey(0)

    kernel = np.ones((2, 3), np.uint8)
    dilatacion = cv2.dilate(umbral, kernel, iterations=1)
    #cv2.imshow('dilatacion', dilatacion)
    #cv2.waitKey(0)
    erosion = cv2.erode(dilatacion, kernel, iterations=1)
    #cv2.imshow('Erosion', erosion)
    #cv2.waitKey(0)
    texto = pytesseract.image_to_string(dilatacion, config=config.PYTESSERACT_CONFIG)
    
    texto_limpio = re.sub(r'\W+', ' ', texto)
    return texto_limpio
