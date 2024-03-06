import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('Photos/park.jpg')
cv.imshow('Actual',img)

# plt.imshow(img)
# plt.show()
#OPENCV-BGR whereas in geneal its RGB

#BGR TO GRAY
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR TO HSV(Hue Saturation Value)
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#BGR TO L*a*b
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LABD',lab)

#BGR TO RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB colour',rgb)


#HSV TO BGR
hsv2bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV-->BGR',hsv2bgr)

#LAB TO BGR
lab2bgr=cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('LAB-->BGR',lab2bgr)

#if GRAYSCALE TO LAB then GRAYSCALE --> BGR and BGR --> LAB
# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)