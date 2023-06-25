import pyautogui
import queue
import time
import pydirectinput
import data
from random import randint

q = queue.Queue()

queueTimer = 0.01


def queueOperator():
	while (data.MOUSE == 1):
		time.sleep(queueTimer)
		if q.empty() != True:
			cmd = q.get()
			if cmd != None:
				if cmd[0] == 'move':
					pyautogui.moveTo(cmd[1], cmd[2])
					time.sleep(cmd[3])
					pyautogui.click(button='right')
					time.sleep(cmd[3])
				elif cmd[0] == 'click':
					time.sleep(2 * cmd[4])
					pyautogui.moveTo(cmd[1], cmd[2])
					time.sleep(2 * cmd[4])
					for i in range(0, cmd[3]):
						time.sleep(cmd[4] + (randint(5, 25) / 1000))
						pyautogui.click(cmd[1], cmd[2], button='right')
				elif cmd[0] == 'LMB':
					# print("LMB !!!")
					pyautogui.moveTo(cmd[1], cmd[2])
					time.sleep(cmd[3])
					pyautogui.click(button='left')
					time.sleep(cmd[3])
				elif cmd[0] == 'write':
					time.sleep(cmd[2])
					pyautogui.write(cmd[1], interval=0.04)
				elif cmd[0] == 'space':
					time.sleep(cmd[3]/2)
					pyautogui.click(cmd[1], cmd[2], button='right')
					time.sleep(cmd[3] * 1.5)
					for i in range(0, cmd[4]):
						time.sleep(cmd[3] * randint(1, 2)+(randint(3,13)/1000))
						pydirectinput.press('space')
				elif cmd[0] == 'mount':
					pydirectinput.keyDown('ctrl')  # Przytrzymaj klawisz Control (Ctrl)
					time.sleep(cmd[2])
					pydirectinput.press('g')
					time.sleep(cmd[2])
					pydirectinput.press('g')
					time.sleep(cmd[2])
					pydirectinput.keyUp('ctrl')  # Zwolnij klawisz Control (Ctrl)
					print("Test")