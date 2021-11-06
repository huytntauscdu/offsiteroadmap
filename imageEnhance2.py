import cv2
import numpy as np
import matplotlib.pyplot as plt


img= cv2.imread('Map1.png')
img1=cv2.imread('Map1.png')
images=np.concatenate(img(img,img1),axis=1)
cv2.imshow("Images",images)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

hist=cv2.calcHist(gray_img,[0],None,[256],[0,256])
hist1=cv2.calcHist(gray_img1,[0],None,[256],[0,256])
plt.subplot(121)
plt.title("Image1")
plt.xlabel('bins')
plt.ylabel("No of pixels")
plt.plot(hist)
plt.subplot(122)
plt.title("Image2")
plt.xlabel('bins')
plt.ylabel("No of pixels")
plt.plot(hist1)
plt.show()

gray_img_eqhist=cv2.equalizeHist(gray_img)
gray_img1_eqhist=cv2.equalizeHist(gray_img1)
hist=cv2.calcHist(gray_img_eqhist,[0],None,[256],[0,256])
hist1=cv2.calcHist(gray_img1_eqhist,[0],None,[256],[0,256])
plt.subplot(121)
plt.plot(hist)
plt.subplot(122)
plt.plot(hist1)
plt.show()

eqhist_images=np.concatenate((gray_img_eqhist,gray_img1_eqhist),axis=1)
cv2.imshow("Images",eqhist_images)
cv2.waitKey(0)
cv2.destroyAllWindows()

clahe=cv2.createCLAHE(clipLimit=40)
gray_img_clahe=clahe.apply(gray_img_eqhist)
gray_img1_clahe=clahe.apply(gray_img1_eqhist)
images=np.concatenate((gray_img_clahe,gray_img1_clahe),axis=1)
cv2.imshow("Images",images)
cv2.waitKey(0)
cv2.destroyAllWindows()