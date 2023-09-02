import cv2
import imutils

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

vs=cv2.VideoCapture(0)

while True:
    _,frame=vs.read()
    frame1=imutils.resize(frame, width=960, height=540)
    cv2.imshow("picture", frame1)
    key=cv2.waitKey(1)
    if key==27:

        break


def recText(frame1):
    text = pytesseract.image_to_string(frame1)
    return text

info = recText(frame1)
print(info)

file = open("result.txt","w")
file.write(info)
file.close()
print("Written Successful")
vs.release()
cv2.destroyAllWindows()