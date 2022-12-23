from flask import Flask, render_template
import cv2
import matplotlib.pyplot as plt
import numpy as np
# import rgb2gray
from skimage.color import rgb2gray

app = Flask(__name__)

@app.route("/")
def main():        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)