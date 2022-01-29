import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("saltpepper.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#homogeneous filter is the most simple filter, each output pixel is the mean of its kernel neighbors
kernel = np.ones((5,5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)

#averaging
blur = cv2.blur(img, (5,5))

#gaussian filter is nothing but using differnet-weight-kernel, in both x and y direction
g_blur = cv2.GaussianBlur(img, (5,5),0)
#this is specially for removing the high frequency noise form the image

#median filter is something that replace each pixel's value with the median of its meighboring pixels.
#this method is great when dealing with "salt and pepper noise"
median = cv2.medianBlur(img, 5 )

#bilateral filter
#the edges details are reserved in this even after smoothing the image
bilateralFiler = cv2.bilateralFilter(img, 9, 75,75)

titles = ['images', "2D Convolution","blur","g_blur","median","bilateralFiler"]
images =[img, dst, blur, g_blur, median,bilateralFiler  ]

for i in range(6):
    plt.subplot(2,3, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
