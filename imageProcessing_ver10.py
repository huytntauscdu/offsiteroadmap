import cv2
import numpy as np
from skimage.transform import hough_line, hough_line_peaks
import matplotlib.pyplot as plt


height = 224
width = 224
min_line_length = 100
max_line_gap = 10

img = cv2.imread('map6.PNG', cv2.CV_8UC1)

resized_img = cv2.resize(img, (height, width))
img_copy = resized_img.copy()
edges = cv2.Canny(resized_img, threshold1 = 50, threshold2 = 150)
lines = cv2.HoughLinesP(edges, rho = 1, theta = np.pi / 180, threshold = 100, minLineLength = min_line_length, maxLineGap = max_line_gap)
for line in lines:
    for x1, y1, x2, y2 in line:
            hough_lines_img = cv2.line(resized_img ,(x1,y1),(x2,y2),color = (0,255,0), thickness = 2)
plt.figure(figsize=(15, 8))
#plt.subplot(1, 2, 1).set_title('Original Image', fontsize = font_size); plt.axis('off')   
#plt.imshow(cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB))
#plt.subplot(1, 2, 2).set_title('After Hough Line Transformation', fontsize = font_size); plt.axis('off')   
plt.imshow(cv2.cvtColor(hough_lines_img, cv2.COLOR_BGR2RGB))
plt.show()