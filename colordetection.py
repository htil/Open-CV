# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 17:18:52 2018

@author: Student
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow('img',cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('HSV','img',0,169,nothing)
cv2.createTrackbar('S','img',0,255,nothing)
cv2.createTrackbar('V','img',0,255,nothing)
cv2.createTrackbar('SLow','img',0,255,nothing)
cv2.createTrackbar('SHigh','img',0,255,nothing)
cv2.createTrackbar('VLow','img',0,255,nothing)
cv2.createTrackbar('VHigh','img',0,255,nothing)


while (1):
    _, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    j = cv2.getTrackbarPos('HSV','img')
    k = cv2.getTrackbarPos('S','img')
    l = cv2.getTrackbarPos('V','img')
    m = cv2.getTrackbarPos('SLow','img')
    n = cv2.getTrackbarPos('SHigh','img')
    o = cv2.getTrackbarPos('VLow','img')
    p = cv2.getTrackbarPos('VHigh','img')
    lower = np.array([j-10,k-m,l-o])
    upper = np.array([j+10,k+n,l+p])
    

    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    if cv2.waitKey(1) & 0xFF == ord('c'):
       print (lower)
       print(upper)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()