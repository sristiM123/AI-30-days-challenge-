import cv2
img= cv2.imread('Sample1.jpg',0)
cv2.imshow('beauty',img)
cv2.imwrite('beauty.jpg',img)
cv2.imread('beauty.jpg',0)
cv2.waitKey(0)
cv2.destroyAllWindows()
