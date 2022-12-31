import cv2
import numpy as np
from random import randint
from ImageProcessing import ImageProcess


def saveImg(img,path):
    with open(path, 'wb') as f:
        f.write(img)

def get_combined(option,edges1,edges2, uniform_phase_bool,uniform_Magnitude_bool):
    img_1 = ImageProcess(edges1,(option == "option1"),1,uniform_phase_bool,uniform_Magnitude_bool)
    img_2 = ImageProcess(edges2,(option != "option1"),2,uniform_phase_bool,uniform_Magnitude_bool)
    img_combined= ImageProcess.combine(img_1.fourier(),img_2.fourier())
    path_img = f"static/images/output/{randint(1,100000)}.png"
    cv2.imwrite(path_img,img_combined)
    return path_img

