import pytesseract
import cv2
import spacy
from fastapi import UploadFile
import numpy as np

nlp = spacy.load("en_core_web_sm")

def anonymize_image(file: UploadFile):
    data = file.file.read()
    arr = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    text = pytesseract.image_to_string(img)
    doc = nlp(text)
    # TODO: detect bounding boxes and redact entities in the image
    _, buf = cv2.imencode('.png', img)
    return buf.tobytes()
