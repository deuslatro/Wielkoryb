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
#from matplotlib import pyplot as plt

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False
# GLOBAL VARIABLES
########################################################################
pustybit = (0, 15, 255)  # Wartosc bita "maski"
chatBitN = np.array([255, 230, 168])  # Wartosc bita "maski"
chatBit = (255, 230, 168)
RESTART_COUNT = 0  # licznik ile razy boty łącznie zostaly zrestartowane podczas aktualneej sesji
THREAD = 1  # Zmienna do konczenia wszystkich watkow (STOP botow)
WHICHTHREAD = 0  # ustalanie ktory watek odpalony za pomoca nazwy

screenGrab = d3dshot.create(capture_output="numpy")
OPEN = 0
PRINTSCREEN = 0
REMOVE_TRASH = 0
RESOLUTION = 0  # 1=640:360 / 800:600 rozdzielczość klienta
fish_Delay = int(data.DATA.get("Fish_Delay"))
space_Delay = int(data.DATA.get("Space_Delay"))
until_Restart = int(data.DATA.get("until_Restart"))
fish_Delay = fish_Delay / 1000
space_Delay = space_Delay / 1000
print(fish_Delay)
print(space_Delay)
print(until_Restart)


def update():
	global OPEN
	OPEN = int(data.DATA.get("Otwieraj_Ryby"))
	global PRINTSCREEN
	PRINTSCREEN = int(data.DATA.get("Zapis_Screenow"))
	global REMOVE_TRASH
	REMOVE_TRASH = int(data.DATA.get("Usuwaj_Smieci"))
	global RESOLUTION  # 1=640:360 / 800:600 rozdzielczość klienta
	RESOLUTION = int(data.DATA.get("Rozdzielczosc_Klienta"))


# wczytanie grafik
ryby = data.load_images_toPIL('img/ryby/')
sample = data.load_images_toPIL('img/samples/')
smieci = data.load_images_toPIL('img/smieci/')
chat = data.load_images_toPIL('img/chat/')
numpyData = data.load_images_toNUMPY('img/numpy')

update()


class BotPosition(Enum):
	TOP_LEFT = 1
	TOP_RIGHT = 2
	BOTTOM_LEFT = 3
	BOTTOM_RIGHT = 4


def find_logo(botPosition):
	logo = sample["logo.png"]
	box3 = logo.getbbox()
	img = ImageGrab.grab()
	screenSize = [0, 0, img.size[0], img.size[1]]
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
	h = 0
	print(
		f"dla watku {threading.current_thread().name}  obszar poszukiwań: szerokosc: {screenSize[0]} {screenSize[2]} wysokosc: {screenSize[1]} {screenSize[3]}")
	for a in range(screenSize[0], (screenSize[2])):
		for b in range(screenSize[1], (screenSize[3])):
			cordinate2 = a, b
			cordinate1 = 0, 0
			if (img.getpixel(cordinate2)) == (logo.getpixel(cordinate1)):
				print("pierwszy pixel zgodny")
				for j in range(0, box3[2]):
					for i in range(0, box3[3]):
						cordinate1 = j, i
						cordinate3 = j + cordinate2[0], i + cordinate2[1]
						if img.getpixel(cordinate3) == logo.getpixel(cordinate1):
							h = h + 1
							if (h == box3[2] + 1 * box3[3] + 1):
								print("znaleziono Logo gry")
								return cordinate3
						else:
							print("blad zgodnosci pixela: ", h)
							h = 0
							break
	return 0


# szuka danej bitmapy w danym obszarze i zwraca jej prawy dolny(?) rog jako koordynaty [uwzglednia maske (pusty bit)]
def szukajwoknie(oknostart, okno, szukany):
	box1 = szukany.getbbox()
	img = ImageGrab.grab(bbox=oknostart + okno)
	szer = okno[0] - oknostart[0]
	wys = okno[1] - oknostart[1]
	sum = box1[2] * box1[3]
	for a in range(0, szer):
		for b in range(0, wys):
			cordinate2 = a, b
			cordinate1 = 0, 0
			if (img.getpixel(cordinate2)) == (szukany.getpixel(cordinate1)):
				# print(f'perwszy bit zgodny w:    :   {szukany.filename}')
				h = 1
				a = 0
				for j in range(0, box1[2]):
					if (a == 1):
						break
					for i in range(0, box1[3]):
						if (h == sum):
							pozycja = cordinate3[0] + oknostart[0], cordinate3[1] + oknostart[1]
							return pozycja
						else:
							cordinate1 = j, i
							cordinate3 = j + cordinate2[0], i + cordinate2[1]
							if szukany.getpixel(cordinate1) == pustybit:
								# print("pusty")
								h = h + 1
								continue
							else:
								# print("zgodny",szukany.filename)
								if cordinate3[0] >= szer or cordinate3[1] >= wys:
									h = 0
									a = 1
									# print("POZA INDEKSEM")
									break
								if img.getpixel(cordinate3) == szukany.getpixel(cordinate1):
									h = h + 1
									if (h == sum):
										pozycja = cordinate3[0] + oknostart[0], cordinate3[1] + oknostart[1]
										return pozycja
								else:
									h = 0
									a = 1
									break
	return 0


def numpyFinder(sectorXY, sectorXY2, sample):
	img = screenGrab.screenshot(region=(sectorXY[0], sectorXY[1], sectorXY2[0], sectorXY2[1]))
	color_filter_20 = np.array([255, 230, 168])
	color_filter_30 = np.array([0, 15, 255])
	img[np.all(img != color_filter_20, axis=-1)] = color_filter_30
	result = cv2.matchTemplate(img, sample, cv2.TM_SQDIFF_NORMED)
	mn, _, mnLoc, _ = cv2.minMaxLoc(result)
	# print("Podobienstwo :", mn, threading.current_thread().name)

	if mn == 0:
		#nie dziala wielowatkowo (tylko do sprawdzania)
		#plt.imshow(img)
		#plt.show()
		return (1, img)
	return (0, 0)


def numpyWhichNumber(sample, img):
	result = cv2.matchTemplate(img, sample, cv2.TM_SQDIFF_NORMED)
	mn, _, mnLoc, _ = cv2.minMaxLoc(result)
	# print("Podobienstwo :", mn, threading.current_thread().name)
	if mn == 0:
		return 1
	else:
		return 0


def czytajCHAT(oknoChatSTART, oknoChatEND):
	(szukaj, img) = numpyFinder(oknoChatSTART, oknoChatEND, numpyData.get('lowienie.npy'))
	if (szukaj != 0):
		for x in range(1, 6):
			if numpyWhichNumber(sample=numpyData.get(f'{x}.npy'), img=img) != 0:
				print(f"Znaleziono {x} na Chacie ", threading.current_thread().name)
				return x
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
	update()
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


def usun(oknostart, okno, oknoeq1, oknoeq2):
	print("brak usuwania")


def initialization(ActualThreadNumber):
	try:
		(oknostart1, okno1, oknoMaleS1, oknoMale1, oknoeqS1, oknoeq1, ekwipunek1) = checkboxy(ActualThreadNumber)
	except TypeError:
		print(f"Brak Loga badz eq/chatu {BotPosition(ActualThreadNumber).name}")
		return 0

	global INFO1
	global INFO2
	print("ilosc restartow: ", RESTART_COUNT)
	koordyrobaka1 = szukajwoknie(oknostart1, okno1, sample["robak.png"])
	if (koordyrobaka1 == 0):
		print(f"Brak robaka watek {BotPosition(ActualThreadNumber).name}")
		data.STATUS[ActualThreadNumber - 1] = "ERR(ROBAK)"
		time.sleep(10)
		initialization(ActualThreadNumber)

	# szukaj lowienia
	wedka = szukajwoknie(oknostart1, okno1, sample["low.png"])
	if (wedka == 0):
		print(f"nie znaleziono wedki w watku {BotPosition(ActualThreadNumber).name}")
		data.STATUS[ActualThreadNumber - 1] = "ERR(WEDKA)"
		time.sleep(10)
		initialization(ActualThreadNumber)

	print(f"ZNALEZIONO ROBAKA I LOWIENIE W WATKU {BotPosition(ActualThreadNumber).name}")
	data.STATUS[ActualThreadNumber - 1] = "START"
	fishing(ActualThreadNumber, koordyrobaka1, wedka, oknoMaleS1, oknoMale1)


def fishing(ActualThreadNumber, koordyrobaka1, koordylowienia1, oknoMaleS1, oknoMale1):
	global RESTART_COUNT
	while THREAD == 1:
		time.sleep(4)
		data.STATUS[ActualThreadNumber - 1] = "ŁOWIE"
		mouse.q.put(('move', koordyrobaka1[0], koordyrobaka1[1], fish_Delay))

		mouse.q.put(('move', koordylowienia1[0], koordylowienia1[1], fish_Delay))

		time.sleep(8)
		fish_Loop = 0
		restart_Counter = 0
		while (fish_Loop == 0):
			fish_Loop = szukajliczb(restart_Counter, oknoMaleS1, oknoMale1)
			restart_Counter = restart_Counter + 1
			if THREAD != 1:
				data.STATUS[ActualThreadNumber - 1] = "STOPOWANKO"
				break
			if fish_Loop == 7:
				RESTART_COUNT += 1
				data.STATUS[ActualThreadNumber - 1] = "RESTART"
				time.sleep(5)
				initialization(ActualThreadNumber)
			if fish_Loop > 0:
				data.STATUS[ActualThreadNumber - 1] = f"FOUND {fish_Loop}"
				mouse.q.put(('click', koordylowienia1[0], koordylowienia1[1], fish_Loop, space_Delay))
				time.sleep(5.5)
	return 0


def szukajliczb(restart_Counter, oknoCHAT1, oknoCHAT2):
	# ilosc  prob przed restartem
	if (restart_Counter > until_Restart):
		return 7
	else:
		wynik = czytajCHAT(oknoCHAT1, oknoCHAT2)
	return wynik


def threads_stop(ActualThreadNumber):
	time.sleep(4)
	data.THREAD_STOP = 1
	data.STATUS[ActualThreadNumber - 1] = "OFF"


def stop():
	global THREAD
	THREAD = 0


def checkboxy(ActualThreadNumber):
	koordyLoga1 = find_logo(ActualThreadNumber)
	update()
	if koordyLoga1 == 0:
		print(f"BRAK LOGA W WATKU {BotPosition(ActualThreadNumber).name}")
		data.STATUS[ActualThreadNumber - 1] = "ERR(LOGO)"
		return 0

	if RESOLUTION == 1:
		okno1 = koordyLoga1[0] + 620, koordyLoga1[1] + 380
	else:
		okno1 = koordyLoga1[0] + 820, koordyLoga1[1] + 630

	ekipunek1 = szukajwoknie(koordyLoga1, okno1, sample["eq.png"])
	if ekipunek1 == 0:
		print(f"nie znaleziono ekwipunku w watku {BotPosition(ActualThreadNumber).name}")
		data.STATUS[ActualThreadNumber - 1] = "ERR(EQ)"
		return 0
	else:
		# pozycja wzgledem probki eq[ikany DOPALACZE]
		print("znaleziono EQ")
		oknoeqS1 = ekipunek1[0] + 15, ekipunek1[1] - 70
		# rozmiar
		oknoeq1 = oknoeqS1[0] + 165, oknoeqS1[1] + 295

	chat = szukajwoknie(koordyLoga1, okno1, sample["chat.png"])
	if chat == 0:
		print(f"nie znaleziono CHATU w watku {BotPosition(ActualThreadNumber).name}")
		data.STATUS[ActualThreadNumber - 1] = "ERR(CHAT)"
		if threading.current_thread().name != "MainThread":
			return 0

	else:
		print("znaleziono CHAT")
		# pozycja wzgledem probki protokołu chatu[ikony wyślij wiadomość]
		oknoCHATS1 = chat[0] - 355, chat[1] - 28
		# rozmiar
		oknoCHAT1 = oknoCHATS1[0] + 60, oknoCHATS1[1] + 14

	if PRINTSCREEN == 1:
		img = ImageGrab.grab(bbox=None)
		draw = ImageDraw.Draw(img)
		rysujokno1 = koordyLoga1 + okno1
		rysujeq1 = oknoeqS1 + oknoeq1
		if chat != 0:
			rysujchat1 = oknoCHATS1 + oknoCHAT1
		boxS = oknoeqS1[0] + 14, oknoeqS1[1] + 22
		boxE = boxS[0] + 9, boxS[1] + 9
		rysujDebugg = boxS + boxE
		if RESOLUTION == 1:
			boxS = koordyLoga1[0] + 465, koordyLoga1[1] + 355
			boxE = boxS[0] + 10, boxS[1] + 10
		else:
			boxS = koordyLoga1[0] + 552, koordyLoga1[1] + 597
			boxE = boxS[0] + 7, boxS[1] + 7
		printLowDebug = boxS + boxE
		# rysowanie
		draw.rectangle(rysujokno1, outline=128, width=3)
		draw.rectangle(rysujeq1, outline=(64, 255, 128), width=3)
		draw.rectangle(rysujDebugg, outline=(128, 255, 96), width=1)
		draw.rectangle(printLowDebug, outline=(128, 255, 96), width=1)
		img.save("boxy.png")
		time.sleep(0.5)
		if chat != 0:
			draw.rectangle(rysujchat1, outline=(0, 255, 255), width=3)

	if threading.current_thread().name != "MainThread":
		return koordyLoga1, okno1, oknoCHATS1, oknoCHAT1, oknoeqS1, oknoeq1, ekipunek1
	return koordyLoga1, okno1, oknoeqS1, oknoeq1, ekipunek1


def probka(a):
	try:
		(koordyLoga1, okno1, oknoeqS1, oknoeq1, ekipunek1) = checkboxy(1)

		# Obszar pobierania próbki(dla lowianie (F4))
		if a == sample["low.png"]:
			if RESOLUTION == 1:
				boxS = koordyLoga1[0] + 465, koordyLoga1[1] + 355
				boxE = boxS[0] + 7, boxS[1] + 7
			else:
				boxS = koordyLoga1[0] + 552, koordyLoga1[1] + 597
				boxE = boxS[0] + 7, boxS[1] + 7
			img = ImageGrab.grab(bbox=boxS + boxE)
			img.save(f"img/samples/low.png")
			sample["low.png"] = img
			print("zmieniono low")
		else:
			boxS = oknoeqS1[0] + 14, oknoeqS1[1] + 22
			boxE = boxS[0] + 9, boxS[1] + 9
			img = ImageGrab.grab(bbox=boxS + boxE)

		if a == sample["robak.png"]:
			img.save(f"img/samples/robak.png")
			sample["robak.png"] = img
			print("zmieniono robaka")
		for key in ryby:
			if a == ryby[key]:
				img.save(f"img/ryby/{key}")
				ryby[key] = img
				print("zmieniono rybe")

			break
	except UnboundLocalError:
		print("Otworz EQ !")
