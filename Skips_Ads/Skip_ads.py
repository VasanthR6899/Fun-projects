# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 19:52:45 2022

@author: vasan
"""

import cv2
import pyautogui
import numpy as np
import time
#import pynput

#time.sleep(20)
screen_resolution=tuple(pyautogui.size())
fps=15
count=0
#image=cv2.imread(r"C:\Users\vasan\OneDrive\Desktop\projects\Screenshot 2022-01-02 154519.png")
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = (r"C:\Users\vasan\OneDrive\Desktop\projects\Recording.avi")

#img=pyautogui.screenshot(r"C:\Users\vasan\OneDrive\Desktop\projects\pytest.jpg")

out=cv2.VideoWriter(filename,codec,fps,screen_resolution)

while True:
    img=pyautogui.screenshot()
    loc=pyautogui.locateCenterOnScreen(r"C:\Users\vasan\OneDrive\Desktop\projects\skipads.jpg",confidence=0.5)
    try:
        count=count+1
        pyautogui.click(loc[0],loc[1])
    except TypeError:
        print("none type error occured\n")
    frame=np.array(img)
    out.write(frame)
    cv2.namedWindow("output",cv2.WINDOW_NORMAL)
    cv2.resize(frame,(600,600))
    cv2.imshow("output",frame)
    
    if(cv2.waitKey(1)==ord('q')):
        break
    
out.release()
cv2.destroyAllWindows()