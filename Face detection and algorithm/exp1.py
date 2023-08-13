import cv2, os

alg='Face detection and algorithm\haarcascades_haarcascade_frontalface_default.xml'

dataset='dataset'
sub_data='subdata'
path=os.path.join(dataset,sub_data)
if not os.path.join(dataset,sub_data):
    os.mkdir(path)
haar_cascade=cv2.CascadeClassifier(alg)

cam=cv2.VideoCapture(0)

count=0
print("No face Detected")

while count<31:
    print(count)
    _,img=cam.read()
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=haar_cascade.detectMultiScale(grayImg,1.3,4)
    
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        faceOnly=grayImg[y:y+h,x:x+w]
        resizeImg=cv2.resize(faceOnly,(200,200))
        cv2.imwrite("%s/%s.jpg"%(path,count),resizeImg)
        count+=1
    cv2.imshow("FaceDetection",img)
    key=cv2.waitKey(10)
    
    if key==27:
        break
print("Image Captured Successfully")
cam.release()
cv2.destroyAllWindows()
