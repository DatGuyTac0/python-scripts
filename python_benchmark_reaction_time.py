import pyautogui
target_color = (119, 216, 119)
while True:
     x, y = pyautogui.position()
     color = pyautogui.pixel(x, y)
     if color == target_color:
        pyautogui.click()