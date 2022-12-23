from flask import Flask, render_template
import cv2
import matplotlib.pyplot as plt
import numpy as np
# import rgb2gray
from skimage.color import rgb2gray

img_1=cv2.imread(r"static/images/man.jpg")
img_1=rgb2gray(img_1)
img_2=cv2.imread(r"static/images/bird.jpg")
img_2=rgb2gray(img_2)
img_1=cv2.resize(img_1 ,(640 , 426))
img_2=cv2.resize(img_2 ,(640 , 426))
filename="static/images/man1.jpg"
cv2.imwrite(filename, img_1)
#resize image and change it to gray scale
# plt.imshow(img_1 , cmap='gray')
# plt.savefig("static/images/man1.jpg")
# plt.imshow(img_2, cmap='gray')
# plt.savefig("static/images/bird1.jpg")
# plt.switch_backend('agg')


#plotting section
# fig=plt.figure(figsize=(10,7))
# fig.add_subplot(1,2,1)
# fig.add_subplot(1,2,2)
# plt.show()
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

# fig=plt.figure(figsize=(10,7))
# fig.add_subplot(2,2,1)
# plt.title("magnitude image 2")
# plt.imshow(np.log(mag_2), cmap='gray')
# fig.add_subplot(2,2,2)
# plt.title("phase image 2")
# plt.imshow(phase_2,cmap='gray')
# fig.add_subplot(2,2,3)
# plt.title("magnitude image 1")
# plt.imshow(np.log(mag_1) , cmap='gray')
# fig.add_subplot(2,2,4)
# plt.title("phase image 1")
# plt.imshow(phase_1,cmap='gray')
# plt.show()

mag_1_phase_sphinx= np.multiply((mag_1), np.exp(1j*phase_2))
mag_shpin_phase_1= np.multiply((mag_2), np.exp(1j*phase_1))

img_combined=np.real(np.fft.ifft2(np.fft.ifftshift(mag_1_phase_sphinx)))
img_combined_2=np.real(np.fft.ifft2(np.fft.ifftshift(mag_shpin_phase_1)))

# fig=plt.figure(figsize=(10,7))
# fig.add_subplot(2,2,1)
# plt.imshow(img_combined , cmap='gray')    
# fig.add_subplot(2,2,2)
# plt.imshow(img_combined_2 , cmap='gray')