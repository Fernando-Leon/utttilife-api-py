
import os
from flask import request, jsonify
from werkzeug.utils import secure_filename
from app import app
from app.image_processing import process_image
from config import Config

UPLOAD_FOLDER = 'uploads/'

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
        texto_1, texto_2 = process_image(filepath, Config)
        
        # Opcional: eliminar la imagen después de procesarla
        os.remove(filepath)
        
        return jsonify({'texto_1': texto_1, 'texto_2': texto_2})
