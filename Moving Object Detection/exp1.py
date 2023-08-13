import cv2
img= cv2.imread("Moving Object Detection\Sample1.JPG")
guasianBlurImg = cv2.GaussianBlur(img,(21,21),0)
cv2.imshow("GaussianBlur",guasianBlurImg)
grayImg = cv2.cvtColor(guasianBlurImg,cv2.COLOR_BGR2GRAY)
cv2.rectangle(img,(0,0),(100,100),(0,255,0),3)
cv2.putText(img,"Hello World",(0,130),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
cv2.imwrite("Moving Object Detection\Sample1Gray.JPG",guasianBlurImg)
cv2.imshow("Gray",guasianBlurImg)
cv2.destroyAllWindows()

