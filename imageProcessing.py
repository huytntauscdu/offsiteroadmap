import cv2 as cv

# Read in an image
img = cv.imread('Map1.png')
#cv.imshow('map1', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

# Blur 
blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
#cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (9,9), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
#eroded = cv.erode(dilated, (3,3), iterations=3)


cv.waitKey(0)