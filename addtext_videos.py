import cv2
import datetime

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#cap.set(cv2.CAP_PROP_FRAME_HEIGHT,3000)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3000)
#properties can also be written as numbers. each number show specific properties
#print(cap.get(3))
#print(cap.get(4))
 
while(cap):
    ret, frame= cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_PLAIN
        #for priting height and width on the video
        text= "Width:" + str(cap.get(3))+ " Height: "+ str(cap.get(4))
        frame = cv2.putText(frame,text, (10,50), font,1, (0,255,255),2, cv2.LINE_AA )

        #for printing date and time on the video
        datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, (10, 100), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

        #showing frames/ video
        cv2.imshow("frame", frame)

        #if we press 'q', the video wil close
        if cv2.waitKey(1) == ord("q"):
            break
    else:
        break

cap.release() #releasing all the elements of cap object
cv2.destroyAllWindows()