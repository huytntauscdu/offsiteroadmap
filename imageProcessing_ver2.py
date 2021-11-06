import cv2 as cv
import numpy as np
from skimage.transform import hough_line, hough_line_peaks

img = cv.imread('map5.PNG')

#cv.imshow('cat', img)


# Converting to grayscale
gray = cv.cvtColor(img,50,150, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# Blur 
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)


# Dilating the image
dilated = cv.dilate(blur, (7,7), iterations=3)
#cv.imshow('Dilated', dilated)

# Eroding
#eroded = cv.erode(dilated, (7,7), iterations=3)
#cv.imshow('Eroded', eroded)

# Edge Cascade
canny = cv.Canny(dilated, 125, 150)
cv.imshow('Canny Edges', canny)


# apply image thresholding
ret, thresh = cv.threshold(canny, 130, 145, cv.THRESH_BINARY)






minLineLength = 100
maxLineGap = 5
lines = cv.HoughLinesP(canny,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv.imshow('Hough Line', img)
#cv.imwrite('map_result1.png',img)


contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')


cv.waitKey(0)