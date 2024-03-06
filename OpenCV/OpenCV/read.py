import cv2 as cv

#how to read images
'''
img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat',img)
cv.waitKey(0)
'''

#how to read videos

capture= cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue,frame=capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()

