import cv2
img= cv2.imread('Sample1.jpg',0)
cv2.imshow('beauty',img)
cv2.imwrite('beauty.jpg',img)
cv2.imread('beauty.jpg',0)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
img=cv2.imread('sample2.jpg',1)
print(img.shape)
print(img.size)
print(img.dtype)


img=cv2.imread('sample2.jpg',1)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("Sample2.jpg", gray)
cv2.imshow("Sample2.jpg", gray)
cv2.imshow("Sample2.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
