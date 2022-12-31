import cv2
import numpy as np


class Image:

    def __init__(self,img):
        if type(img) is str : 
            self.img = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
        else:
            self.img = img

    def grayScale(self):
        pass
    
    def resize(self,width=640,height= 427):
        self.img =  cv2.resize(self.img,(width,height))
    
    def fourier(self):
        fourier_= np.fft.fft2((self.img)) #fft2 for 2d fourier transform as the variation of the image happend in two dimension 
        fourier_shifted = np.fft.fftshift(fourier_) # to avoid the repeation in the frequencies
        return fourier_shifted
 
    def save(self,path):
        with open(path, 'wb') as f:
            cv2.imwrite(path,self.img)

        


class ImageProcessing:
    def __init__(self,edges,value,uniform_Magnitude_bool,uniform_phase_bool,img):
        self.edges = edges
        self.value = value
        self.uniform_Magnitude_bool = uniform_Magnitude_bool
        self.uniform_phase_bool = uniform_phase_bool
        self.img = img


    def handleFourier(self):
        self.img.grayScale()
        self.img.resize()
        return self.img.fourier()


    def __crop(self,arr):
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                if (i < self.edges[0][0] or i>=self.edges[0][1] )or (j<=self.edges[1][0] or j >=self.edges[1][1] ): #the i and j axis are obtined according to the cropped image
                    arr[i][j]=self.value
        return arr
        
    def __handel_croper(self):
        fourier_shifted = self.handleFourier()
        if self.value == 1:
            arr_=np.abs(fourier_shifted) # the magnitude after fourier
            arr_ = self.__crop(arr_)
            if self.uniform_Magnitude_bool=="true":
                arr_ = np.ones(arr_.shape)
                     
        elif self.value == 0:
            arr_=np.angle(fourier_shifted)# the phase after fourier
            arr_ = self.__crop(arr_)
            if self.uniform_phase_bool == 'true':
                arr_ = np.zeros(arr_.shape)
            arr_ = np.exp(1j*arr_)
        self.img = arr_ 

        

        
    def get_cropped(self):
        self.__handel_croper()
        return self.img

            
    def multiply(self,img2):
        return np.multiply(self.img,img2)

    def combine(self,img2):
        return np.real(np.fft.ifft2(np.fft.ifftshift(self.multiply(img2.img))))

    

    









