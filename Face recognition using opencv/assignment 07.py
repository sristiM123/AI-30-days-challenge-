import cv2
import os
import urllib.request
import numpy
import imutils
size = 4
haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'dataset'
print('Training...')
(images, labels, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(datasets):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(datasets, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            label = id
            images.append(cv2.imread(path, 0))
            labels.append(int(label))
        id += 1
(width, height) = (130, 100)
(images, labels) = [numpy.array(lis) for lis in [images, labels]]
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, labels)
face_cascade = cv2.CascadeClassifier(haar_file)
url = "http://192.168.0.102:8080/img.jpg"
webcam = cv2.VideoCapture(0)
cnt=0
while True:
    imgpath = urllib.request.urlopen(url)
    imgnp = numpy.array(bytearray(imgpath.read()), dtype=numpy.uint8)
    img = cv2.imdecode(imgnp, -1)
    img = imutils.resize(img, width=450)
    if ord('q') == cv2.waitKey(1):
        exit(0)
    cnt = 0
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        prediction = model.predict(face_resize)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        if prediction[1]<800:
            cv2.putText(img,'%s - %.0f' % (names[prediction[0]],prediction[1]),(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(255, 0, 0))
            print (names[prediction[0]])
            cnt=0
        else:
            cnt+=1
            cv2.putText(img,'Unknown',(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1,(0, 255, 0))
            if(cnt>100):
                print("Unknown Person")
                cv2.imwrite("input.jpg",img)
                cnt=0
    cv2.imshow('OpenCV', img)
    key = cv2.waitKey(10)
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()