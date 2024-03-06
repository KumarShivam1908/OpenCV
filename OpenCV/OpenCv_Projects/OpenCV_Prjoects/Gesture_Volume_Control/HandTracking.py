import cv2 as cv
import mediapipe as mp
import time

cap=cv.VideoCapture(0)
wcam,hcam=1080,1080
cap.set(3, wcam)
cap.set(4, hcam)

mpHands = mp.solutions.hands
hands=mpHands.Hands() #USES RGB ONLY
mpDraw=mp.solutions.drawing_utils

Ptime=0
Ctime=0

while True:
    isSuccess,img=cap.read()
    img_RGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results=hands.process(img_RGB)
    print(results.multi_hand_landmarks)

    Ctime=time.time()
    fps=1/(Ctime-Ptime)
    Ptime=Ctime

    cv.putText(img,f"FPS:{int(fps)}",(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

    cv.imshow("img",img)
    cv.waitKey(1)

if __name__ == "__main__":
    main()