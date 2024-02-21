

from flask import jsonify
from app import app
from app.utils.upload import upload_file

@app.route('/upload', methods=['POST'])
def handle_upload():
    return upload_file()
