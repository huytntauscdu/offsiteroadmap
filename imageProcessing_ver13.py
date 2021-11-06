import cv2 # For CV operations
from PIL import Image  #To create and store images
import numpy as np

#To binarize the input
import h5py
import os


imageNameStorage = '123'
dim = (256, 256) #(w,h)

readImage = cv2.imread('map6.PNG')
print("Reading Image : " + str(readImage) +" with Index : ")

resizedImage = cv2.resize(readImage, dim, interpolation=cv2.INTER_AREA)
imageName = str(readImage).split(".")[0]
print("Shape of resized Image is : ", resizedImage.shape)

cv2.imwrite(imageNameStorage + ".png", resizedImage)
print("Resized and Stored Image : " + str(resizedImage) +" with Index : ")


(thresh, im_bw) = cv2.threshold(resizedImage, 128, 255, cv2.THRESH_BINARY)  
print("Shape of resized Image is : ", im_bw.shape)

images = []