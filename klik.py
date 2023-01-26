import time
import pyautogui

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

time.sleep(5)
for i in  range(1,1000):
	pyautogui.click(button='right')