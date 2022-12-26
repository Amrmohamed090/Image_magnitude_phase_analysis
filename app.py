from flask import Flask , render_template,request
from flask_cors import CORS
import matplotlib.pyplot as plt
import numpy as np
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
        print(f'image1:::: x1{request.form["img1_x1"]} x2:{request.form["img1_x2"]} y1:{request.form["img1_y1"]} y2:{request.form["img1_y2"]}')
        print(f'image2:::: x1{request.form["img2_x1"]} x2:{request.form["img2_x2"]} y1:{request.form["img2_y1"]} y2:{request.form["img2_y2"]}')
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