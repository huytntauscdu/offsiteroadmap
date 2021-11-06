import cv2
import matplotlib.pyplot as plt

img = cv2.imread('map6.PNG')
height, width, channel = img.shape
# we use fastNlMeansDenoisingColored to reduce the noise
noise_reduced_image = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

# now we will resize the image to a smaller size like 500, 500
H, W = 500, 500
noise_reduced_image_resized = cv2.resize(noise_reduced_image, (H, W))

# we keep the original ratio to the image to calculate the bounding box sizes
height_ratio = height/H
width_ratio = width/W

plt.show()
