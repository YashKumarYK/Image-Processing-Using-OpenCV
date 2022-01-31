##pyramid
#pyramid, or pyramid representation, is a type of multi-scale signal representation in which a signal or an image is subject to repeated smoothing and subsampling
#two types of pyramid: 1. Gaussian pyramid 2. Laplacian pyramid
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("Sohil_copy.png")
# lr1 = cv2.pyrDown(img)
# lr2 = cv2.pyrDown(lr1)
# lr3 = cv2.pyrUp(lr2)
# cv2.imshow("Original Image", img)
# cv2.imshow("pyrdown1 Image", lr1)
# cv2.imshow("pyrdown2 Image", lr2)
# cv2.imshow("pyrup Image", lr3  )
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i), layer)

#A level in laplacian pyramid is formed by the difference between that level in gaussian pyramid and the expanded version of its upper level in gaussian pyramid
layer = gp[5]
cv2.imshow("Upper level Gaussian pyramid", layer)
lp = [layer]
for i in range(5,0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()