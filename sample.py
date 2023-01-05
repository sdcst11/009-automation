import pyautogui as p
import time

while True:
    icon = p.locateCenterOnScreen("assets/gimp.png")
    print(icon)
    while icon != None:
        p.moveTo(icon)
        p.click()
    time.sleep(0.25)