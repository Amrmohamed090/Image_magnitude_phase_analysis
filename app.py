from flask import Flask , render_template, redirect,url_for,request,send_from_directory,session,jsonify, make_response
from flask_cors import CORS
import cv2
import matplotlib.pyplot as plt
import numpy as np
# import rgb2gray
from skimage.color import rgb2gray
import os
import base64
import combine


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

CORS(app)


@app.route("/",methods=["GET","POST"])
def main():
    if request.method == "POST":
        imgdata1 = base64.b64decode(request.form["imgdata1"].split(',')[1])
        imgdata2 = base64.b64decode(request.form["imgdata2"].split(',')[1])
        filename1 = './static/images/cropped1.png'  # I assume you have a way of picking unique filenames
        filename2 = './static/images/cropped2.png'  # I assume you have a way of picking unique filenames
        with open(filename1, 'wb') as f:
            f.write(imgdata1)
        with open(filename2, 'wb') as f:
            f.write(imgdata2)
        combine.get_combined()
      
        
       # with open("imageToSave.png", "wb") as fh:
        #    fh.write(base64.decodebytes(request.form[0]))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)