import pyautogui
import queue
import time
import data


q = queue.Queue()

queueTimer=0.1

def queueOperator():
	while(data.MOUSE==1):
		time.sleep(queueTimer)
		if q.empty()!=True:
			cmd = q.get()
			if cmd != None:
				if cmd[0] == 'move':
					pyautogui.moveTo(cmd[1],cmd[2])
					time.sleep(cmd[3])
					pyautogui.click(button='right')
					time.sleep(cmd[3])
				elif cmd[0] == 'click':
					time.sleep(2*cmd[4])
					pyautogui.moveTo(cmd[1], cmd[2])
					time.sleep(2*cmd[4])
					for i in range(0,cmd[3]):
						time.sleep(cmd[4])
						pyautogui.click(button='right')
						time.sleep(cmd[4])
				elif cmd[0] == 'LMB':
					print("LMB !!!")
					pyautogui.moveTo(cmd[1], cmd[2])
					time.sleep(cmd[4])
					pyautogui.click(button='left')
					time.sleep(cmd[4])


