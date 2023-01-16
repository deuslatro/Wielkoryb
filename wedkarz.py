import asyncio
import time
import threading
import pyautogui
import numpy as np
import cv2
from PIL import ImageGrab, ImageDraw, Image
from enum import Enum
import d3dshot
import data
import mouse
from random import randint
import disbot
import findFunctions

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False
# GLOBAL VARIABLES
########################################################################
pustybit = (0, 15, 255)  # Wartosc bita "maski"
# chatBit = (255, 230, 168)
RESTART_COUNT = 0  # licznik ile razy boty łącznie zostaly zrestartowane podczas aktualneej sesji
THREAD = 1  # Zmienna do konczenia wszystkich watkow (STOP botow)
WHICHTHREAD = 0  # ustalanie ktory watek odpalony za pomoca nazwy
exitConversationLoop = 0
screenGrab = d3dshot.create(capture_output="numpy")

#   POZYCJONOWANIE OBSZAROW BOTA   #
# rozdzielczosc gry(jakiej wielkosci jest okno gry w ktorym bot ma szukac)
GameSize600 = 600, 380
GameSize800 = 820, 620
# eq (wielkosc oraz pozycja eq wzgledem wyszukanej ikonki/ znaku)
EQ_COORDS = -25, 95
EQ_SIZE = 165, 305  # szerokosc / wysokosc
# probka (1 slot w eq)
SAMPLE_COORDS = 19, 10
SAMPLE_SIZE = 9, 9  # szerokosc / wysokosc
# ikonka lowienia(slot f4 zalezny od rozdzielczosci klienta)
# ikonka MSG(prawa strona zalezna od rozdzielczosci klienta)
MSG_COORDS = 0, 20
MSG_SIZE = 10, 100  # szerokosc / wysokosc
# okno chatu(fragment w ktorym wyszukuje wiadomosci)
CHAT_COORDS = -400, -9  # pozycja wzgledem probki
CHAT_SIZE = 48, 10  # szerokosc / wysokosc
# okno chmurki(fragment w ktorym wyszukuje chmurki z liczba)
CLOUD_COORDS = 370, 215  # pozycja wzgledem loga
CLOUD_SIZE = 45, 45  # szerokosc / wysokosc

BIOLOG = 0
OPEN = 0
PRINTSCREEN = 0
DISCORD_BOT = 0
RESOLUTION = 1  # 1=640:360 / 800:600 rozdzielczość klienta
if RESOLUTION == 1:
	GameSize = 800, 600
else:
	GameSize = 640, 360
NUMBER_OF_SCANNED_LINE = 1
AUTO_EXIT = 0
AUTO_MSG = 1
ALL_AUTO_EXIT = 0

fish_Delay = int(data.DATA.get("Fish_Delay"))
space_Delay = int(data.DATA.get("Space_Delay"))
until_Restart = int(data.DATA.get("until_Restart"))
fish_Delay = fish_Delay / 1000
space_Delay = space_Delay / 1000
print('opoznienie lowienia:', fish_Delay)
print('opoznienie wylawiania(odstep miedzy spacjiami):', space_Delay)
print('iteracji do RESTARTU:', until_Restart)
lock = threading.Lock()
eventLoop = asyncio.get_event_loop()

color_filter_10 = np.array([198, 195, 198])  # Kolor pixeli wiadomosci prywatnej(ikony)
color_filter_20 = np.array([255, 230, 186])  # Kolor tekstu INFORMACJI w cliencie


def updateConfig():
	global OPEN
	OPEN = int(data.DATA.get("Otwieraj_Ryby"))
	global PRINTSCREEN
	PRINTSCREEN = int(data.DATA.get("Zapis_Screenow"))
	global DISCORD_BOT
	DISCORD_BOT = int(data.DATA.get("Discord_Bot"))
	global RESOLUTION  # 1=640:360 / 800:600 rozdzielczość klienta
	RESOLUTION = int(data.DATA.get("Rozdzielczosc_Klienta"))


# wczytanie grafik
ryby = data.load_images_toPIL('img/ryby/')
sample = data.load_images_toPIL('img/samples/')
smieci = data.load_images_toPIL('img/smieci/')
chat = data.load_images_toPIL('img/chat/')
numpyData = data.load_images_toNUMPY('img/numpy')

np.save('img/numpy/lowienie.npy', np.array(chat.get('lowienie.png')))
np.save('img/numpy/1.npy', np.array(chat.get('1.png')))
np.save('img/numpy/2.npy', np.array(chat.get('2.png')))
np.save('img/numpy/3.npy', np.array(chat.get('3.png')))
np.save('img/numpy/4.npy', np.array(chat.get('4.png')))
np.save('img/numpy/5.npy', np.array(chat.get('5.png')))
np.save('img/numpy/msg.npy', np.array(chat.get('msg.png')))
updateConfig()


class BotPosition(Enum):
	TOP_LEFT = 1
	TOP_RIGHT = 2
	BOTTOM_LEFT = 3
	BOTTOM_RIGHT = 4


def lineSpacing(chatWindow):
	teampList = list(chatWindow)
	teampList[1] = teampList[1] - 15
	teampList[3] = teampList[3] - 15
	chatWindow = tuple(teampList)
	return chatWindow


# Wyszukuje w oknie o podanych koordach oraz wielkosci wszystkie pixele jednakowego koloru na takiej samej pozycji


# def numpyWhichNumber(sample, img):
# 	result = cv2.matchTemplate(img, sample, cv2.TM_SQDIFF_NORMED)
# 	mn, _, mnLoc, _ = cv2.minMaxLoc(result)
# 	#print("Podobienstwo :", mn, threading.current_thread().name)
# 	if mn == 0:
# 		return 1
# 	else:
# 		return 0

def readCHAT(chatWindow):
	for line in range(0, NUMBER_OF_SCANNED_LINE):
		chatWindow = lineSpacing(chatWindow)
		(szukaj, img) = findFunctions.numpyFinder(chatWindow, numpyData.get('lowienie.npy'), color_filter_20)
		if (szukaj != 0):
			print("SUCCES")
			img2 = img[2:10, 40:46, :]
			for findnumber in range(2, 6):
				if findFunctions.numpyWhichNumber(sample=numpyData.get(f'{findnumber}.npy'), img=img2) != 0:
					return findnumber
	return 0


def whichThread():
	if threading.current_thread().name == "TOP_LEFT":
		return 1
	elif threading.current_thread().name == "TOP_RIGHT":
		return 2
	elif threading.current_thread().name == "BOTTOM_LEFT":
		return 3
	elif threading.current_thread().name == "BOTTOM_RIGHT":
		return 4
	else:
		print("BLAD URUCHOMIONO 5 watek bota ?")


def start():
	global THREAD
	ActualThreadNumber = whichThread()
	print("NAZWA BOTA: ", threading.current_thread().name)
	updateConfig()
	THREAD = 1
	initialization(ActualThreadNumber)
	print("Koniec dzialania bota", threading.current_thread().name)
	threads_stop(ActualThreadNumber)
	return 0


def startNewBots(numberOfBots: int):
	for botNumber in range(1, numberOfBots + 1):
		time.sleep(0.8)
		thread = threading.Thread(target=start, name=BotPosition(botNumber).name, daemon=True)
		thread.start()


def initialization(ActualThreadNumber):
	try:
		(logoPosition, gameWindow, chatWindow1, msgBox, eqWindow,cloudWindow) = checkBox(ActualThreadNumber)
	except TypeError:
		print(f"Brak Loga badz eq/chatu {BotPosition(ActualThreadNumber).name}")
		return 0
	wholeWindow = logoPosition + gameWindow
	print("ilosc restartow: ", RESTART_COUNT)
	baitPosition = findFunctions.searchInWindow(eqWindow, sample["robak.png"])
	if (baitPosition == 0):
		print(f"Brak robaka watek {BotPosition(ActualThreadNumber).name}")
		data.STATUS[ActualThreadNumber - 1] = "ERR(ROBAK)"
		time.sleep(10)
		initialization(ActualThreadNumber)

	if BIOLOG == 1:
		biologPosition = findFunctions.searchInWindow(wholeWindow, sample["biolog.png"])
		if (biologPosition == 0):
			print(f"Brak biologa ignorowanie {BotPosition(ActualThreadNumber).name}")
	else:
		biologPosition = 0

	# fishingPosition = findFunctions.searchInWindow(wholeWindow, sample["low.png"])
	# if (fishingPosition == 0):
	# 	print(f"nie znaleziono wedki w watku {BotPosition(ActualThreadNumber).name}")
	# 	data.STATUS[ActualThreadNumber - 1] = "ERR(WEDKA)"
	# 	time.sleep(10)
	# 	initialization(ActualThreadNumber)

	data.STATUS[ActualThreadNumber - 1] = "START"
	fishing(ActualThreadNumber, chatWindow1, msgBox, wholeWindow, biologPosition, baitPosition)


def fishing(ActualThreadNumber, chatWindow1, msgBox, wholeWindow, biologPosition, baitPosition):
	global RESTART_COUNT
	while THREAD == 1:
		data.STATUS[ActualThreadNumber - 1] = "ŁOWIE"
		time.sleep(5)
		print(baitPosition)
		mouse.q.put(('move', baitPosition[0], baitPosition[1], fish_Delay))
		# for key in ryby:
		# 	fishPosition = findFunctions.searchInWindow(eqWindow, ryby[key])
		# 	if fishPosition != 0:
		# 		mouse.q.put(('move', fishPosition[0], fishPosition[1], fish_Delay))
		# 		break

		with lock:
			if DISCORD_BOT == 1:
				(msgIconPosition, _) = findFunctions.numpyFinder(msgBox, numpyData.get('msg.npy'), color_filter_10)
				if msgIconPosition != 0:
					print("WIADOMOSC MSG")
					msgIconPosition = msgIconPosition[0] + msgBox[0], msgIconPosition[1] + msgBox[1]
					conversation(msgIconPosition, ActualThreadNumber, wholeWindow)

		# mouse.q.put(('move', fishingPosition[0], fishingPosition[1], fish_Delay))
		# if biologPosition != 0:
		# 	time.sleep(0.2)
		# 	mouse.q.put(('LMB', biologPosition[0], biologPosition[1],1, fish_Delay))

		time.sleep(7.5)
		data.STATUS[ActualThreadNumber - 1] = "SZUKAM"
		fish_Loop = 0
		restart_Counter = 0
		while fish_Loop == 0:
			fish_Loop = searchInChat(restart_Counter, chatWindow1)
			restart_Counter += 1
			if THREAD != 1:
				data.STATUS[ActualThreadNumber - 1] = "STOPOWANKO"
				break
			if fish_Loop == 7:
				RESTART_COUNT += 1
				data.STATUS[ActualThreadNumber - 1] = "RESTART"
				time.sleep(5)
				initialization(ActualThreadNumber)
				break
			if fish_Loop > 0:
				with lock:
					data.STATUS[ActualThreadNumber - 1] = f"FOUND {fish_Loop}"
				# mouse.q.put(('click', baitPosition[0], baitPosition[1], 1, space_Delay))
				# zmiana na SPACJE
				# mouse.q.put(('click', fishingPosition[0], fishingPosition[1], fish_Loop, space_Delay))
				time.sleep(5.5)
	return 0


def exitGame(ActualThreadNumber):
	img = ImageGrab.grab()
	screenSize = [0, 0, img.size[0], img.size[1]]
	screenSize = botWindowPosition(screenSize, ActualThreadNumber, img)
	exitButton1 = findFunctions.searchInWindow(screenSize, sample["exit1.png"])
	mouse.q.put(('LMB', exitButton1[0], exitButton1[1], 1, space_Delay))
	time.sleep(3)
	mouse.q.put(('LMB', exitButton1[0] - 280, exitButton1[1] - 110, 1, space_Delay))
	time.sleep(5)


def chatBot(ActualThreadNumber):
	time.sleep(4)
	if ActualThreadNumber == 1:
		# msgInGame(ActualThreadNumber, '   ')
		msgInGame(ActualThreadNumber, 'cze')
		time.sleep(5)
	# msgInGame(ActualThreadNumber, '   ')
	# msgInGame(ActualThreadNumber, 'zw kibl')
	if ActualThreadNumber == 2:
		msgInGame(ActualThreadNumber, 'elo')
		# msgInGame(ActualThreadNumber, '   ')
		time.sleep(5)
	# msgInGame(ActualThreadNumber, 'tez masz takie lagi?')
	# msgInGame(ActualThreadNumber, '   ')
	if ActualThreadNumber == 3:
		msgInGame(ActualThreadNumber, 'siema')
		# msgInGame(ActualThreadNumber, '   ')
		time.sleep(5)
	# msgInGame(ActualThreadNumber, 'o luj ktora godz ja spadam')
	# msgInGame(ActualThreadNumber, '   ')
	if ActualThreadNumber == 4:
		msgInGame(ActualThreadNumber, 'yo')
		# msgInGame(ActualThreadNumber, '   ')
		time.sleep(5)


# msgInGame(ActualThreadNumber, 'tez ci tak laguje?')
# msgInGame(ActualThreadNumber, '   ')


def conversation(msgIconPosition, ActualThreadNumber, wholeWindow):
	disbot.exitConversationLoop = 1
	future = asyncio.run_coroutine_threadsafe(disbot.client.signal(f"@here  Wiadomosc w watku:{ActualThreadNumber}"),
	                                          eventLoop)
	future.result()
	mouse.q.put(('LMB', msgIconPosition[0], msgIconPosition[1], 1, space_Delay))
	time.sleep(3)
	msgWindowPosition = findFunctions.searchInWindow(window=wholeWindow, szukany=sample['msg2.png'])
	print(msgWindowPosition)
	msgWindowBox = msgWindowPosition[0] - 280, msgWindowPosition[1] - 130, msgWindowPosition[0], msgWindowPosition[1]
	if AUTO_MSG:
		chatBot(ActualThreadNumber)
		time.sleep(0.5)

	screen = ImageGrab.grab(bbox=msgWindowBox)
	future = asyncio.run_coroutine_threadsafe(disbot.client.sendScreen(screen), eventLoop)
	future.result()

	if ALL_AUTO_EXIT:
		for botsID in range(1, 5):
			exitGame(botsID)
	elif AUTO_EXIT:
		exitGame(ActualThreadNumber)

	while disbot.exitConversationLoop == 1:
		pass
	print("koniec rozmowy")


# print("wiadomosc w watku ",ActualThreadNumber)

def searchInChat(restart_Counter, chatWindow):
	# ilosc  prob przed restartem
	if (restart_Counter > until_Restart):
		return 7
	else:
		wynik = readCHAT(chatWindow)
	return wynik


def threads_stop(ActualThreadNumber):
	time.sleep(4)
	data.STATUS[ActualThreadNumber - 1] = "OFF"


def stop():
	global THREAD
	THREAD = 0


def checkBox(ActualThreadNumber):
	logoPosition = findFunctions.find_logo(ActualThreadNumber, sample["logo.png"])
	updateConfig()
	if logoPosition == 0:
		print(f"BRAK LOGA W WATKU {BotPosition(ActualThreadNumber).name}")
		data.STATUS[ActualThreadNumber - 1] = "ERR(LOGO)"
		return 0,0,0,0,0,0
	gameWindow = logoPosition[0] + GameSize[0], logoPosition[1] + GameSize[1]
	eqPosition = findFunctions.searchInWindow(logoPosition + gameWindow, sample["eq.png"])
	if eqPosition == 0:
		print(f"nie znaleziono ekwipunku w watku {BotPosition(ActualThreadNumber).name}")
		data.STATUS[ActualThreadNumber - 1] = "ERR(EQ)"
		eqWindow = 0
	else:
		# pozycja wzgledem probki eq[handel postaciami]
		eqWindow = eqPosition[0] + EQ_COORDS[0], eqPosition[1] + EQ_COORDS[1], eqPosition[0] + EQ_COORDS[0] + EQ_SIZE[
			0], eqPosition[1] + EQ_COORDS[1] + EQ_SIZE[1]

	chat = findFunctions.searchInWindow(logoPosition + gameWindow, sample["chat.png"])
	if chat == 0:
		print(f"nie znaleziono CHATU w watku {BotPosition(ActualThreadNumber).name}")
		data.STATUS[ActualThreadNumber - 1] = "ERR(CHAT)"
		chatWindow = 0
	else:
		# pozycja wzgledem probki protokołu chatu[ikony wyślij wiadomość]
		chatWindow = chat[0] + CHAT_COORDS[0], chat[1] + CHAT_COORDS[1], chat[0] + CHAT_COORDS[0] + CHAT_SIZE[0], chat[
			1] + CHAT_COORDS[1] + CHAT_SIZE[1]
	if RESOLUTION == 1:
		msgBox = logoPosition[0] + MSG_COORDS[0], logoPosition[1] + MSG_COORDS[1], logoPosition[0] + MSG_COORDS[0] + \
		         MSG_SIZE[0], logoPosition[1] + MSG_COORDS[1] + MSG_SIZE[1]
	else:
		msgBox = logoPosition[0] + MSG_COORDS[0], logoPosition[1] + MSG_COORDS[1], logoPosition[0] + MSG_COORDS[0] + \
		         MSG_SIZE[0], logoPosition[1] + MSG_COORDS[1] + MSG_SIZE[1]


	if RESOLUTION == 1:
		cloudWindow = logoPosition[0] + CLOUD_COORDS[0], logoPosition[1] + CLOUD_COORDS[1], logoPosition[0] + CLOUD_COORDS[0] + \
		         CLOUD_SIZE[0], logoPosition[1] + CLOUD_COORDS[1] + CLOUD_SIZE[1]
	else:
		cloudWindow = logoPosition[0] + CLOUD_COORDS[0], logoPosition[1] + CLOUD_COORDS[1], logoPosition[0] + CLOUD_COORDS[0] + \
		         CLOUD_SIZE[0], logoPosition[1] + CLOUD_COORDS[1] + CLOUD_SIZE[1]


	if PRINTSCREEN == 1:
		img = ImageGrab.grab(bbox=None)
		draw = ImageDraw.Draw(img)
		printWindow = logoPosition + gameWindow
		if eqWindow == 0:
			print("EQ ERR")
			printEQ = 0
		else:
			printEQ = eqWindow
			printDebug = eqWindow[0] + SAMPLE_COORDS[0], eqWindow[1] + SAMPLE_COORDS[1], eqWindow[0] + SAMPLE_COORDS[
				0] + SAMPLE_SIZE[0], eqWindow[1] + SAMPLE_COORDS[1] + SAMPLE_SIZE[1]
		if RESOLUTION == 1:
			printFishDebug = logoPosition[0] + 465, logoPosition[1] + 355, logoPosition[0] + 472, logoPosition[1] + 362
		else:
			printFishDebug = logoPosition[0] + 555, logoPosition[1] + 590, logoPosition[0] + 560, logoPosition[1] + 600
		# rysowanie
		draw.rectangle(printWindow, outline=128, width=3)
		if printEQ != 0:
			draw.rectangle(printDebug, outline=(128, 255, 96), width=1)
			draw.rectangle(printEQ, outline=(64, 255, 128), width=3)

		draw.rectangle(msgBox, outline=(16, 255, 255), width=2)
		draw.rectangle(cloudWindow, outline=(16, 255, 255), width=2)
		draw.rectangle(printFishDebug, outline=(128, 255, 96), width=1)
		if chatWindow != 0:
			for line in range(0, NUMBER_OF_SCANNED_LINE):
				chatWindow = lineSpacing(chatWindow)
				draw.rectangle(chatWindow, outline=(255, 16, 16), width=2)
		img.save("boxy.png")
		time.sleep(0.5)
		if chat != 0:
			draw.rectangle(chatWindow, outline=(0, 255, 255), width=3)

	return logoPosition, gameWindow, chatWindow, msgBox, eqWindow, cloudWindow


def botWindowPosition(screenSize, botPosition, img):
	botPosition = int(botPosition)
	if botPosition == 1:
		screenSize[2] = int(img.size[0] / 2)
		screenSize[3] = int(img.size[1] / 2)
	elif botPosition == 2:
		screenSize[0] = int((img.size[0] / 2) + 1)
		screenSize[3] = int((img.size[1] / 2) + 1)
	elif botPosition == 3:
		screenSize[2] = int(img.size[0] / 2)
		screenSize[1] = int(img.size[1] / 2)
	elif botPosition == 4:
		screenSize[1] = int((img.size[1] / 2) + 1)
		screenSize[0] = int((img.size[1] / 2) + 1)
	else:
		print("brak podanego watku bota")
	return screenSize


def msgInGame(botPosition, tresc):
	img = ImageGrab.grab()
	screenSize = [0, 0, img.size[0], img.size[1]]
	screenSize = botWindowPosition(screenSize, botPosition, img)
	send = findFunctions.searchInWindow(screenSize, sample["msg2.png"])
	if send == 0:
		print("brak otwartej wiadomosci w oknie")
	else:
		mouse.q.put(('move', send[0] - 35, send[1], 1, space_Delay))
		mouse.q.put(('write', tresc, space_Delay))
		mouse.q.put(('LMB', send[0], send[1], 1, space_Delay))
		mouse.q.put(('move', send[0] - 35, send[1], 1, space_Delay))
		print('otwarta waidomosc : ', send)


def closeMsgWindow(botPosition):
	img = ImageGrab.grab()
	screenSize = [0, 0, img.size[0], img.size[1]]
	screenSize = botWindowPosition(screenSize, botPosition, img)
	exitMsg = findFunctions.searchInWindow(screenSize, sample["exitMsg.png"])
	if exitMsg == 0:
		print("brak otwartej wiadomosci w oknie")
	else:
		mouse.q.put(('LMB', exitMsg[0], exitMsg[1] - 25, 1, space_Delay))


async def picToDiscord(botPosition):
	img = ImageGrab.grab()
	screenSize = [0, 0, img.size[0], img.size[1]]
	screenSize = botWindowPosition(screenSize, botPosition, img)
	sendButton = findFunctions.searchInWindow(screenSize, sample["msg2.png"])
	msgWindowBox = sendButton[0] - 230, sendButton[1] - 130, sendButton[0], sendButton[1]
	screen = ImageGrab.grab(bbox=msgWindowBox)
	await disbot.client.sendScreen(screen)


def probka(a):
	try:
		(logoPosition,_,_,_,eqWindow,_) = checkBox(1)
		# Obszar pobierania próbki(dla lowianie (F4))
		if a == sample["low.png"]:
			if RESOLUTION == 1:
				boxS = logoPosition[0] + 465, logoPosition[1] + 355
				boxE = boxS[0] + 7, boxS[1] + 7
			else:
				boxS = logoPosition[0] + 552, logoPosition[1] + 597
				boxE = boxS[0] + 7, boxS[1] + 7
			print('boxS:', boxS, 'boxE:', boxE)
			img = ImageGrab.grab(bbox=boxS + boxE)
			img.save(f"img/samples/low.png")
			sample["low.png"] = img
			print("zmieniono low")
		else:
			pass
			printDebug = eqWindow[0] + SAMPLE_COORDS[0], eqWindow[1] + SAMPLE_COORDS[1], eqWindow[0] + SAMPLE_COORDS[
				0] + SAMPLE_SIZE[0], eqWindow[1] + SAMPLE_COORDS[1] + SAMPLE_SIZE[1]
			print(printDebug)
			boxS = printDebug[0], printDebug[1]
			boxE = printDebug[2], printDebug[3]
			print('boxS:', boxS, 'boxE:', boxE)
			img = ImageGrab.grab(bbox=boxS + boxE)

		if a == sample["robak.png"]:
			img.save(f"img/samples/robak.png")
			sample["robak.png"] = img
			print("zmieniono robaka")
		for key in ryby:
			if a == ryby[key]:
				print(a)
				img.save(f"img/ryby/{key}")
				ryby[key] = img
				print("zmieniono rybe")
				break
	except Exception as e:
		print('Exception Sample:', repr(e))
