import pytesseract
import re
import numpy as np
from PIL import Image, ImageEnhance
from flask import Flask, request, jsonify
import cv2

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return('Hi, This is OCR KTM PCR API for extract NIM')
    
@app.route('/predict', methods=['POST'])
def extract_nim():
    file = request.files['image']
    # Membaca gambar menggunakan PIL
    image = Image.open(file.stream)
    contrast = ImageEnhance.Contrast(image)
    img=contrast.enhance(2)
    img = np.asarray(img)
    r, g, b = cv2.split(img)
    contrast=cv2.merge([b, g, r])
    # Preprocessing
    # get grayscale image
    gray = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
    
    # noise removal
    noise = cv2.medianBlur(gray,5)
    
    #thresholding
    thresh = cv2.threshold(noise, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    # Mengenali teks dari gambar menggunakan Tesseract OCR
    text = pytesseract.image_to_string(thresh)
    
    # Mencocokkan pola teks menggunakan regex untuk mendapatkan deretan angka 10 digit
    pattern = r'\b\d{10}\b'
    result = re.findall(pattern, text)
    
    # Joinkan result agar menjadi nim
    response = ''.join(result)
    
    # Mengembalikan hasil ekstraksi deretan angka 10 digit sebagai respons HTTP
    return jsonify(nim=response)