#DINOSAUR CHEAT GOOGLE!!!!!!!

from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import time
import keyboard
from numpy import *

replaybtn = (960, 438)
dinosaur = (724, 456)



def restartGame():
    pyautogui.click(replaybtn)
    print("Happy Jumping Dino!")


def image_grab():
    box = (dinosaur[0]+55, dinosaur[1], dinosaur[0]+145, dinosaur[1]+5)
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
