# app/image_processing.py

import cv2
import pytesseract
import re
from app.ocr.ocr_black import ocr_black_part
from app.ocr.ocr_white import ocr_white_part

def process_image(filepath, config, umbral_inv=True):
    imagen = cv2.imread(filepath)
    texto_1 = ocr_white_part(imagen, config,umbral_inv)
    texto_2 = ocr_black_part(imagen, config)
    return texto_1, texto_2
