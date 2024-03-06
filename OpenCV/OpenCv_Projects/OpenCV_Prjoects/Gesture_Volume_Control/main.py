import cv2
import cv2 as cv
import numpy as np
import time
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wcam, hcam = 1080, 480
cap = cv.VideoCapture(0)

cap.set(3, wcam)
cap.set(4, hcam)
pTime = 0

detector=htm.handDetector(detectionConfidence=0.7)



# Get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# Get current volume
# volume.GetMute()
# volume.GetMasterVolumeLevel()
vol_range=volume.GetVolumeRange()
volume.SetMasterVolumeLevel(-5.0,None)
minVol=vol_range[0]
maxVol=vol_range[1]
volBar=400
vol=0
volper=0

# Capture image
while True:
    success, img = cap.read()

    img = detector.findHands(img)
    lmlist=detector.findPosition(img,draw=False)
    if len(lmlist) != 0:
        # print(lmlist[4],lmlist[8])

        x1,y1=lmlist[4][1],lmlist[4][2]
        x2,y2=lmlist[8][1],lmlist[8][2]

        cx,cy=(x1+x2)//2,(y1+y2)//2

        cv.circle(img,(x1,y1),15,(255,0,255),cv.FILLED)
        cv.circle(img,(x2,y2),15,(255,0,255),cv.FILLED)
        cv.line(img,(x1,y1),(x2,y2),(255,0,255),3)
        cv.circle(img,(cx,cy),15,(255,0,255),cv.FILLED)

        length=math.hypot(x2-x1,y2-y1)
        # print(length)

        # Hand Range 30-300
        #Volumne range: -65 to 0

        vol=np.interp(length,[50,300],[minVol,maxVol])
        volBar=np.interp(length,[50,300],[400,150])
        volper = np.interp(length, [50, 300], [0, 100])
        # print(vol)
        volume.SetMasterVolumeLevel(vol, None)

    cv.rectangle(img,(50,150),(85,400),(0,255,0),3)
    cv.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv.FILLED)

    # FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Draw FPS text
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, f' {int(volper)}%', (40, 50), font, 1.5, (0, 255, 0), 2, cv.LINE_AA)

    cv.imshow("Img", img)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cv.destroyAllWindows()
cap.release()
