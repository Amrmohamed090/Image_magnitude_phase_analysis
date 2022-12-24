import cv2
import numpy as np
from skimage.color import rgb2gray
from random import randint
import os


def get_combined(option):
    img_1=cv2.imread(r"static/images/input/cropped1.png",cv2.IMREAD_GRAYSCALE)
 
    img_2=cv2.imread(r"static/images/input/cropped2.png",cv2.IMREAD_GRAYSCALE)

    x1,y1 = img_1.shape
    x2,y2 = img_2.shape
    x = min(x1,x2)
    y = min(y1,y2)

    img_1=cv2.resize(img_1 ,(x , y))
    img_2=cv2.resize(img_2 ,(x , y))

    #Extraction of frequencies of first image
    
    fourier_1=np.fft.fft2((img_1)) #fft2 for 2d fourier transform as the variation of the image happend in two dimension 
    fourier_1_shifted = np.fft.fftshift(fourier_1) # to avoid the repeation in the frequencies
    mag_1=np.abs(fourier_1_shifted) # the magnitude after fourier
    phase_1=np.angle(fourier_1_shifted)# the phase after fourier
    #Extraction of frequencies of second image
    fourier_2=np.fft.fft2((img_2))
    fourier_2_shifted = np.fft.fftshift(fourier_2) 
    mag_2=np.abs(fourier_2_shifted) 
    phase_2=np.angle(fourier_2_shifted)


    if option == "option1":
        mag_1_phase_sphinx= np.multiply((mag_1), np.exp(1j*phase_2))
    elif option == "option2":
        mag_1_phase_sphinx= np.multiply((mag_2), np.exp(1j*phase_1))

    img_combined=np.real(np.fft.ifft2(np.fft.ifftshift(mag_1_phase_sphinx)))
    
    list_img = os.listdir("static/images/output")
    for img in list_img:
        path = "static/images/output/" + img
        os.remove(path)
    path_img = f"static/images/output/{randint(1,100000)}.png"
    
    cv2.imwrite(path_img,img_combined)
    return path_img
