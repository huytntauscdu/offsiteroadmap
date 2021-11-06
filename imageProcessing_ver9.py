import cv2 as cv
import numpy as np
from skimage.transform import hough_line, hough_line_peaks
import matplotlib.pyplot as plt

height = 224
width = 224

img = cv.imread('map5.PNG', cv.CV_8UC1)


resized_img = cv.resize(img, (height, width))
min_line_length = 100
max_line_gap = 10

denoised_img = cv.medianBlur(resized_img, 5)

th = cv.adaptiveThreshold(resized_img, maxValue = 255, adaptiveMethod = cv.ADAPTIVE_THRESH_GAUSSIAN_C, thresholdType = cv.THRESH_BINARY, blockSize = 11, C = 2)
laplacian = cv.Laplacian(th, cv.CV_64F).astype('uint8')
edges = cv.Canny(th, threshold1 = 1500, threshold2 = 500)

lines = cv.HoughLinesP(edges, rho = 1, theta = np.pi / 180, threshold = 100, minLineLength = min_line_length, maxLineGap = max_line_gap)
for line in lines:
    for x1, y1, x2, y2 in line:
        hough_lines_img = cv.line(resized_img ,(x1,y1),(x2,y2),color = (0,255,0), thickness = 2)


#plt.imshow(cv.cvtColor(resized_img, cv.COLOR_BGR2RGB))
#plt.imshow(resized_img, cmap='gray')
#plt.imshow(cv.cvtColor(denoised_img, cv.COLOR_BGR2RGB))
#plt.imshow(cv.cvtColor(th, cv.COLOR_BGR2RGB))
#plt.imshow(cv.cvtColor(laplacian.astype('float32'), cv.COLOR_BGR2RGB))
#plt.imshow(cv.cvtColor(edges, cv.COLOR_BGR2RGB))
plt.imshow(cv.cvtColor(hough_lines_img, cv.COLOR_BGR2RGB))
plt.show()