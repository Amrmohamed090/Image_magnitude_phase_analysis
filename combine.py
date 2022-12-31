import cv2
import numpy as np
from random import randint
from Imagecombination import *
from Image import *


def saveImg(img,path):
    with open(path, 'wb') as f:
        f.write(img)

def get_combined(option,edges1,edges2, uniform_phase_bool,uniform_Magnitude_bool):
    img_1 = Image(edges1,(option == "option1"),1,uniform_phase_bool,uniform_Magnitude_bool)
    img_2 = Image(edges2,(option != "option1"),2,uniform_phase_bool,uniform_Magnitude_bool)
    ImageProcessing_1 = ImageProcessing(img_1.fourier(),img_2.fourier())
    img_combined = ImageProcessing_1.combine()
    path_img = f"static/images/output/{randint(1,100000)}.png"
    cv2.imwrite(path_img,img_combined)
    return path_img

