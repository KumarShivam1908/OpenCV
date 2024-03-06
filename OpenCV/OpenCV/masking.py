import cv2 as cv
import numpy as np

img=cv.imread("Photos/cats.jpg")
cv.imshow("image",img)

#dimension of mask should be same as that of the image
blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('blank',blank)

mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,thickness=-1)
cv.imshow('Mask',mask)

masked_image=cv.bitwise_and(img,img,mask=mask)
cv.imshow("Masked",masked_image)

cv.waitKey(0)