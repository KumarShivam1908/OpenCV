import cv2 as cv

img=cv.imread('Photos/group 2.jpg')
cv.imshow("lady",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("Gray",gray)

har_casscade=cv.CascadeClassifier('haar_face.xml')
face_rect=har_casscade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=7)

print(f"No of faces detected are {len(face_rect)}")

for(x,y,w,h) in face_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow("Face_detected",img)



cv.waitKey(0)