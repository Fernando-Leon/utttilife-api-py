

from app import app
from config import Config
from app.routes import *

if __name__ == '__main__':
    app.run(debug=Config.DEBUG)
