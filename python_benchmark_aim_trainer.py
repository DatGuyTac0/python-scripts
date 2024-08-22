import time
import cv2
import pyautogui
while True:
    try:
        target = pyautogui.locateOnScreen("target1.png", grayscale=True, confidence=.5)
        pyautogui.moveTo(target)
    except pyautogui.ImageNotFoundException:
        pass