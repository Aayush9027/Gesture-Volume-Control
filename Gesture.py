import handtrackingmodule as htm
import cv2
import time
import numpy as np
import mediapipe as mp
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wCam,hCam=640,480
devices = AudioUtilities.GetSpeakers()#initialization for using pycaw
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange=volume.GetVolumeRange()
minVol=volRange[0]#lower bound in range of values for volume in pycaw
maxVol=volRange[1]#upper bound
vol=0
volbar=400
volperc=0
area=0
colorVol=(255,0,0)
PTime=0# previous time
CTime=0# current time
cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam) 
detector=htm.handDetector(detectionCon=0.7,maxHands=1)
while True:
    success,img=cap.read()#T or F,frame
    
    #find Hand
    img =detector.findHands(img)#using method built in my class
    lmlist,bbox=detector.findPosition(img,draw=True)#method for finding landmark
    if len(lmlist)!=0:#if hand is in front of camera thn only it can show points else none
        #print(lmlist[4],lmlist[8])# we want only thumb(4) and index finger(8) tip
        
        #filter based on size-bounding box
        area=(bbox[2]-bbox[0])*(bbox[3]-bbox[1])//100 #calculating area of box so that after a particular value only our gestures work
        #print(area)
        if 250<=area<=1300:

            #find distance beween index and thumb
            length,img,LineInfo=detector.findDistance(4,8,img)
            #print(length)

            #convert volume
            volbar=np.interp(length,[50,300],[400,150])
            volperc=np.interp(length,[50,300],[0,100])
          
            #smoothning
            smoothness=10
            volperc=smoothness*round(volperc/smoothness)

            #finger up
            fingers=detector.fingersUp()
            #print(fingers)

            #if pinky is down thn set volume
            if not fingers[4]:
               volume.SetMasterVolumeLevelScalar(volperc/100, None)#changing volume of our computer
               cv2.circle(img,(LineInfo[4],LineInfo[5]),15,(0,255,0),cv2.FILLED)#gives button effect,changes color as we are setting volume                
               colorVol=(0,255,0)
            else:
                colorVol=(255,0,0)

    #drawings            
    cv2.rectangle(img,(50,150),(85,400),(255,0,0),3)
    cv2.rectangle(img,(50,int(volbar)),(85,400),(255,0,0),cv2.FILLED)     
    cv2.putText(img,f'{(int(volperc))}%',(40,450),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    cVol=int(volume.GetMasterVolumeLevelScalar()*100)
    cv2.putText(img,f'Vol Set: {int(cVol)}%',(400,50),cv2.FONT_HERSHEY_COMPLEX,1,colorVol,3)
   
   #Frame rate
    CTime=time.time()#current time
    fps=1/(CTime-PTime)#FPS
    PTime=CTime#previous time is replaced by current time

    cv2.putText(img,f'FPS: {str(int(fps))}',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)# showing Fps on screen
    

    cv2.imshow("Image",img)#showing img not imgRGB
    cv2.waitKey(1)