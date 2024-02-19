from flask import Flask, request, jsonify
import cv2
import numpy as np
import pytesseract
import re
from werkzeug.utils import secure_filename
import os
import Test_Images

app = Flask(__name__)

# Configuración personalizada para pytesseract
configuracion = '--oem 3 --psm 12'

# Ruta para guardar las imágenes temporales
UPLOAD_FOLDER = 'uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file EXISTENTE'})
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Procesar la imagen
        imagen = cv2.imread(filepath)
        texto_1 = Test_Images.ocr_white_Parte(imagen, configuracion)
        texto_2 = Test_Images.ocr_Black_parte(imagen, configuracion)
        
        # Opcional: eliminar la imagen después de procesarla
        os.remove(filepath)
        
        return jsonify({'texto_1': texto_1, 'texto_2': texto_2})

if __name__ == '__main__':
    app.run(debug=True)
