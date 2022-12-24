from flask import Flask , render_template, redirect,url_for,request,send_from_directory,session,jsonify, make_response
from flask_cors import CORS
import cv2
import matplotlib.pyplot as plt
import numpy as np
# import rgb2gray
from skimage.color import rgb2gray
import os
import base64
from combine import *
import json

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

CORS(app)


@app.route("/",methods=["GET","POST"])
def main():

    return render_template("index.html")


@app.route('/saveImg',methods =['POST',"GET"])
def save_Img():
    if request.method == "POST":
        option = request.form["option"]
        imgdata1 = base64.b64decode(request.form["imgdata1"].split(',')[1])
        imgdata2 = base64.b64decode(request.form["imgdata2"].split(',')[1])
        filename1 = './static/images/input/cropped1.png'  # I assume you have a way of picking unique filenames
        filename2 = './static/images/input/cropped2.png'  # I assume you have a way of picking unique filenames
        with open(filename1, 'wb') as f:
            f.write(imgdata1)
        with open(filename2, 'wb') as f:
            f.write(imgdata2)
        image_1 = get_combined(option)
    return json.dumps({1: f'<img src="{image_1}"  id="comb_img" alt="" >'})

if __name__ == "__main__":
    app.run(debug=True)