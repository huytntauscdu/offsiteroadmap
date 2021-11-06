1.	from __future__ import print_function
2.	from builtins import input
3.	import cv2 as cv
4.	import numpy as np
5.	import argparse
6.	# Read image given by user
7.	parser = argparse.ArgumentParser(description='Code for Changing the contrast and brightness of an image! tutorial.')
8.	parser.add_argument('--input', help='Path to input image.', default='lena.jpg')
9.	args = parser.parse_args()
10.	image = cv.imread(cv.samples.findFile(args.input))
11.	if image is None:
12.	    print('Could not open or find the image: ', args.input)
13.	    exit(0)
14.	new_image = np.zeros(image.shape, image.dtype)
15.	alpha = 1.0 # Simple contrast control
16.	beta = 0    # Simple brightness control
17.	# Initialize values
18.	print(' Basic Linear Transforms ')
19.	print('-------------------------')
20.	try:
21.	    alpha = float(input('* Enter the alpha value [1.0-3.0]: '))
22.	    beta = int(input('* Enter the beta value [0-100]: '))
23.	except ValueError:
24.	    print('Error, not a number')
25.	# Do the operation new_image(i,j) = alpha*image(i,j) + beta
26.	# Instead of these 'for' loops we could have used simply:
27.	# new_image = cv.convertScaleAbs(image, alpha=alpha, beta=beta)
28.	# but we wanted to show you how to access the pixels :)
29.	for y in range(image.shape[0]):
30.	    for x in range(image.shape[1]):
31.	        for c in range(image.shape[2]):
32.	            new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)
33.	cv.imshow('Original Image', image)
34.	cv.imshow('New Image', new_image)
35.	# Wait until user press some key
36.	cv.waitKey()
37.	 
