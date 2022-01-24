import numpy as np
import cv2

img = cv2.imread("sohil.jpg", -1)
#img= np.zeros([512,512,3], np.uint8)
#line
img = cv2.line(img,(0,0),(234,435), (255,0,0), 5 )

#arraowedline
img= cv2.arrowedLine(img,(0,10),(34,435), (0,255,0), 5)

#rectangle
img= cv2.rectangle(img,( 134,134), (370,370), (0,0,255),5 )

#circle
img= cv2.circle(img, (300,300),150, (100,100,100), 10)

#
font= cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
img = cv2.putText(img, "Sohil mf",(10,500), font, 4, (255,255,255), 10, cv2.LINE_AA )

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()