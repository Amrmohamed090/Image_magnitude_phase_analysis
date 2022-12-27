import cv2
import numpy as np
from skimage.color import rgb2gray
from random import randint
import os
import matplotlib.pyplot as plt

def update(arr,edges,value):
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if (i < edges[0][0] or i>=edges[0][1] )or (j<=edges[1][0] or j >=edges[1][1] ): #the i and j axis are obtined according to the cropped image
                arr[i][j]=value

def get_combined(option,edges1,edges2):
    img_1=cv2.imread(r"static/images/input/original1.png",cv2.IMREAD_GRAYSCALE)
    img_2=cv2.imread(r"static/images/input/original2.png",cv2.IMREAD_GRAYSCALE)

    x1,y1 = img_1.shape
    x2,y2 = img_2.shape
    x = min(x1,x2)
    y = min(y1,y2)
    

    img_1=cv2.resize(img_1 ,(y , x))
    img_2=cv2.resize(img_2 ,(y , x))

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
        update(mag_1,edges1,0)
        update(phase_2,edges2,1)
        mag_1_phase_sphinx= np.multiply((mag_1), np.exp(1j*phase_2))

    elif option == "option2":
        update(mag_2,edges2,0)
        update(phase_1,edges1,1)
        mag_1_phase_sphinx= np.multiply((mag_2), np.exp(1j*phase_1))



    img_combined=np.real(np.fft.ifft2(np.fft.ifftshift(mag_1_phase_sphinx)))


    list_img = os.listdir("static/images/output")
    for img in list_img:
        path = "static/images/output/" + img
        os.remove(path)
    path_img = f"static/images/output/{randint(1,100000)}.png"

    
    cv2.imwrite(path_img,img_combined)
    return path_img
