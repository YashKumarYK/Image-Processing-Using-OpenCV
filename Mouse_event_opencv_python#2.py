import numpy as np
import cv2


def click_event(event, x,y, flags, param):
    if event ==cv2.EVENT_LBUTTONDOWN:
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        #strBGR= str(blue) + ' , ' + str(green) + ' , ' + str(red)
        cv2.circle(img, (x,y), 5, (0,0,255), -1)
        mycolorimage = np.zeros((500,500,3), np.uint8)

        mycolorimage[:] = [blue, green , red]
        cv2.imshow("color", mycolorimage)

#img = np.zeros((550,550,3),np.uint8)
img = cv2.imread("sohil.jpg")
cv2.imshow("image",img)
points =[]

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
