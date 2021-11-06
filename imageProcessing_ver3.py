import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pylab as pylab
from skimage import io
from skimage import color
import cv2 as cv
from skimage.feature import canny
from skimage.filters import sobel

def read_image(filename):
    image = io.imread(filename)
    image = color.rgb2gray(image)
    #image = right_orient_mammogram(image)
    return image


def apply_canny(image):
    canny_img = canny(image, 5)
    return sobel(canny_img)

img = read_image('.\map4.PNG')


gray = apply_canny(img)


cv.imshow('Hough Line', img)
cv.imwrite('houghlines5.jpg',gray)
cv.waitKey(0)

