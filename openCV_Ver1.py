import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('map6.png',0)
blur = cv2.GaussianBlur(img, (3,3), cv2.BORDER_DEFAULT)

#delating the image
dilated = cv2.dilate(blur, (3,3))

edges = cv2.Canny(dilated,125,255)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])



plt.show()