from flask import Flask , request
# from PIL import Image
import pytesseract
from PIL import Image
from gridfs import GridFS
from io import BytesIO
# from pymongo import MongoClient
from flask_pymongo import PyMongo
import cv2
app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/your_database_name"
mongo = PyMongo(app)
fs = GridFS(mongo.db)
import base64
from bson import Binary

@app.route("/mamber", methods=['POST'])
def members():
    if 'file' not in request.files:
        return 'No file part in the request'
    file = request.files['file']
    file_content = file.read()
    pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'
    img = Image.open(BytesIO(file_content))
    
    text = pytesseract.image_to_string(img)
    # mongo.db.images.insert_one({'data': img, 'text': text}).inserted_id
    return {'result': text}
if __name__ == "__main__":
    app.run(debug = True)