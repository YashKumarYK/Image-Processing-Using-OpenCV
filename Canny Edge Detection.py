##canny edge detection
#the canny edge detection is an edge detecion operator that uses a multi-stage algothm to detect a wide range of edges in image
#this algothm is composed of 5 steps:
#1 Noise reduction
#2. Gradient Calculation
#3. Non-maximum suppression
#4. Double threshold
#5 Edge Tracking by hysteresis

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("David.png", 0)

#for laplacian gradient
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)

lap = np.uint8(np.absolute(lap))

#for sobel gradient represention
sobelX = cv2.Sobel(img, cv2.CV_64F, 1,0) # 1: we want to use sobel x method
sobelY =cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

#combining the results of sobel x and sobely
sobelcombined = cv2.bitwise_or(sobelX, sobelY)

#canny edge detection
edge = cv2.Canny(img, 100,200)
titles= ["image", "laplacian gradient", "SobelX", "SobelY", "SobelCombined", "canny"]
images = [img, lap, sobelX, sobelY, sobelcombined,edge]

for i in range (6):
    plt.subplot(2,3, i+1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
