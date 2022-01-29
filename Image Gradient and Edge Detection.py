#gradient-- an image gradient is a directional change in the intensity or color in an image

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("virat.png", 0)
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
titles= ["image", "laplacian gradient", "SobelX", "SobelY", "SobelCombined"]
images = [img, lap, sobelX, sobelY, sobelcombined]


for i in range (5):
    plt.subplot(2,3, i+1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
