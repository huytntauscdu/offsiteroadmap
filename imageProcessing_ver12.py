import cv2
import numpy as np
import console

# load image in grayscale
img = cv2.imread("imap5.PNG", 0)

# get all connected components
_, output, stats, _ = cv2.connectedComponentsWithStats(img, connectivity=4)

# get a list of areas for each group label
group_areas = stats[cv2.CC_STAT_AREA]
# get the id of the group with the largest area (ignoring 0, which is the background id)
max_group_id = np.argmax(group_areas[1:]) + 1

# get max_group_id mask and save it as an image
max_group_id_mask = (output == max_group_id).astype(np.uint8) * 255
cv2.imwrite("output.png", max_group_id_mask)