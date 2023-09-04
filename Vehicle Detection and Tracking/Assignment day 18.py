#Deploy same application with 2 Camera, represents North & South

import cv2
import imutils
cascade_src = r"D:\All Code/practice\AI internship/Vehicle Detection and Tracking/cars.xml"
car_cascade = cv2.CascadeClassifier(cascade_src)
cam_north=cv2.VideoCapture(0)
cam_south=cv2.VideoCapture(2)
while True:
    detected = 0
    _,img1=cam_north.read()
    img1=imutils.resize(img1,width=400) 
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1) 
    for (x,y,w,h) in cars:
        cv2.rectangle(img1,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Frame", img1)
    b=str(len(cars))
    a= int(b)
    detected=a
    n=detected
    print("------------------------------------------------")
    print ("North: %d "%(n))
    if n>=2:
        print ("North More Traffic")
    else:
        print ("no traffic")
    if cv2.waitKey(33) == 27:
        break
    detected2 = 0
    _, img = cam_south.read()  
    img = imutils.resize(img, width=400) 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    cars = car_cascade.detectMultiScale(gray, 1.1, 1) 
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow("Frame", img)
    b = str(len(cars))
    a = int(b)
    detected2 = a
    n = detected2
    print("------------------------------------------------")
    print("South: %d " % (n))
    if n >= 2:
        print("South More Traffic")
    else:
        print("no traffic")
    if cv2.waitKey(44) == 27:
        break
cam_south.release()
cam_north.release()
cv2.destroyAllWindows()