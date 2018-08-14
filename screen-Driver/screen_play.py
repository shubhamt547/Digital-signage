import cv2
#import time
image1=cv2.imread('4.png')
img2=cv2.imread('6.png')

height, width = image1.shape[:2]
print(height,width)
thumbnail = cv2.resize(image1, (width/2, height/2), interpolation = cv2.INTER_AREA)

cv2.imshow('image1',thumbnail)
cv2.waitKey(5000)
cv2.destroyAllWindows()

height, width = img2.shape[:2]

thumbnail1 = cv2.resize(img2, (width/2, height/2), interpolation = cv2.INTER_AREA)

cv2.imshow('img2',thumbnail1)
cv2.waitKey(5000)
cv2.destroyAllWindows()
