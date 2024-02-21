### structure

apipy/                  # Main project directory\
│\
├── app/                # Flask application directory\
│   ├── \_\_init__.py     # Initialization file for the Flask application\
│   ├── image_processing.py # Module for image processing\
│   ├── routes.py       # File for defining application routes\
│   ├── ocr/            # Directory for OCR modules\
│   │   ├── \_\_init__.py # Initialization file for the OCR module\
│   │   ├── ocr_white.py# Module for OCR of white text\
│   │   └── ocr_black.py# Module for OCR of black text\
│   └── utils/          # Directory for utility modules\
│       └── upload.py   # Module for uploading and processing files\
│\
├── config.py           # Configuration file for the Flask application\
└── run.py              # Main file for running the application


### how to run

- step 1: download all dependence on __requirements.txt__ 
- step 2: download Tesseract OCR on your operating system

- step 3: run in a terminal
```shell
flask run
```
