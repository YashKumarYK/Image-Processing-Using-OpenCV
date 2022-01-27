import cv2
import matplotlib.pyplot as plt
#you will see a difference in color of image in both cv2 and matplotlib.
#this is because matplotlib reads the image in rbg and cv2 reads the image in bgr

img = cv2.imread("sohil_copy.png")
cv2.imshow("Image", img)

#this is to convert image in rgb
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
