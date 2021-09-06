#DINOSAUR CHEAT GOOGLE!!!!!!!

from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import time
import keyboard
from numpy import *

rplybtn = (960, 438)
dinosense = (724, 456)



def restartGame():
    pyautogui.click(rplybtn)
    print("Happy Jumping Dino!")


def image_grab():
    box = (dinosense[0]+55, dinosense[1], dinosense[0]+145, dinosense[1]+5)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()

def pressSpace():
    time.sleep(0.1)
    pyautogui.keyDown('space')

time.sleep(4)
restartGame()


while True:
    image_grab()
    if(image_grab() != 697):
       pressSpace()
       time.sleep(0.1)
