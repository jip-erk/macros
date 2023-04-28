import keyboard
import time
import pyautogui


def forward():
    keyboard.release('s')
    keyboard.press('w')
    keyboard.press('d')
 
def backwards():
    keyboard.release('d')
    keyboard.release('w')
    keyboard.press('s')

time.sleep(22)
pyautogui.mouseDown(button='left')

while True:
    forward()
    time.sleep(9)
    backwards()    
    time.sleep(9)