import cv2 as cv

img=cv.imread("Photos/cats.jpg")
cv.imshow("New",img)

#d-It simply takes the average of all the pixels under the kernel area and replaces the central element. This is done by the function cv.blur() or cv.boxFilter().
average=cv.blur(img,(3,3))
cv.imshow('Average_Blur',average)

#Gaussian_blur-In this method, instead of a box filter, a Gaussian kernel is used. It is done with the function, cv.GaussianBlur(). We should specify the width and height of the kernel which should be positive and odd. We also should specify the standard deviation in the X and Y directions, sigmaX and sigmaY respectively.
gauss= cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian_Blur',gauss)

#Median Blur - same as averaging, but instead of averaging it finds median
median=cv.medianBlur(img,3)
cv.imshow('Median_Blur',median)

#Bilateral Blurring- most effective(retain edges+blur)
bilateral=cv.bilateralFilter(img,10 ,35,25)
cv.imshow('Bilateral',bilateral)


cv.waitKey(0)