#morphological transformation are operations based on the image shape
#performed on the binary images

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img_1.png", cv2.IMREAD_GRAYSCALE)

#morphological operations are performd only on binary image,
# here mask is used to convert tha image in binary image using threshold binary
_, mask = cv2.threshold(img, 220,255,cv2.THRESH_BINARY_INV)

kernal = np.ones((2,2), np.uint8)

dilation = cv2.dilate(mask, kernal, iterations=3)
erosion = cv2.erode(mask, kernal , iterations=1)

#in opening , erosion followed by the dilation is opening
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN, kernal)

#dilation is performed first and then erosion
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

#graiend is the difference between dilation and erosion
mg= cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)

#tophat is difference between image and opening of image
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)


titles =['image', 'mask','dilation', 'erosion', 'opening', 'closing', "gradient", 'tophat']
images=[img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2,4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()