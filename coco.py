import keyboard
import time
import pyautogui


# 160 speed ad 43 deg angle

def forward():
    keyboard.release('s')
    keyboard.press('w')
 
def backwards():
    keyboard.release('w')
    keyboard.press('s')

def moveRight():
    keyboard.press('d')
    time.sleep(1)
    keyboard.release('d')

time.sleep(22)
pyautogui.mouseDown(button='left')

while True:
    forward()
    time.sleep(13)
    moveRight()
    backwards()    
    time.sleep(13)
    moveRight()