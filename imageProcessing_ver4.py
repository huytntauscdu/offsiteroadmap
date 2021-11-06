import cv2 as cv
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data
from skimage.color.colorconv import gray2rgb
from skimage.filters import gaussian
from skimage.segmentation import active_contour
from skimage.color.adapt_rgb import adapt_rgb, each_channel, hsv_value
from skimage import filters
from skimage import data
from skimage.exposure import rescale_intensity
import matplotlib.pyplot as plt



img = cv.imread('.\map6.PNG',1)
#img = rgb2gray(img)
img = cv.cvtColor(img,  cv.COLOR_BGR2RGB)

left_nonzero = cv.countNonZero(img[:, 0:int(img.shape[1]/2)])
right_nonzero = cv.countNonZero(img[:, int(img.shape[1]/2):])
if(left_nonzero < right_nonzero):
            img = cv.flip(img, 1)


cv.imshow('map7', img)

@adapt_rgb(each_channel)
def sobel_each(image):
    return filters.sobel(image)


@adapt_rgb(hsv_value)
def sobel_hsv(image):
    return filters.sobel(image)



cv.waitKey(0)