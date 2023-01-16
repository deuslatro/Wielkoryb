import numpy as np
import cv2
from PIL import ImageGrab, ImageDraw, Image
from enum import Enum
import threading
import wedkarz
# do testow czasami przydatne
import matplotlib.pyplot as plt
from mss import mss

sct = mss()

# szuka danej bitmapy w danym obszarze i zwraca jej prawy dolny rog jako koordynaty [uwzglednia maske (pusty bit)]
def searchInWindow(window, szukany):
	# window1 prawy gorny rog okna, window2 lewy dolny
	window1 = (window[0], window[1])
	window2 = (window[2], window[3])
	box1 = szukany.getbbox()
	img = ImageGrab.grab(bbox=window1 + window2)
	szer = window2[0] - window1[0]
	wys = window2[1] - window1[1]
	sum = box1[2] * box1[3]
	cordinate3 = 0, 0
	for a in range(0, szer):
		for b in range(0, wys):
			cordinate2 = a, b
			cordinate1 = 0, 0
			if (img.getpixel(cordinate2)) == (szukany.getpixel(cordinate1)):
				# print(f'perwszy bit zgodny w:    :   {szukany.filename}')
				numberOfCorrectBits = 1
				exitLoopBit = 0
				for j in range(0, box1[2]):
					if (exitLoopBit == 1):
						break
					for i in range(0, box1[3]):
						if (numberOfCorrectBits == sum):
							pozycja = cordinate3[0] + window1[0], cordinate3[1] + window1[1]
							return pozycja
						else:
							cordinate1 = j, i
							cordinate3 = j + cordinate2[0], i + cordinate2[1]
							if szukany.getpixel(cordinate1) == wedkarz.pustybit:
								# print("pusty")
								numberOfCorrectBits = numberOfCorrectBits + 1
								continue
							else:
								# print("zgodny",szukany.filename)
								if cordinate3[0] >= szer or cordinate3[1] >= wys:
									numberOfCorrectBits = 0
									exitLoopBit = 1
									# print("POZA INDEKSEM")
									break
								if img.getpixel(cordinate3) == szukany.getpixel(cordinate1):
									numberOfCorrectBits = numberOfCorrectBits + 1
									if (numberOfCorrectBits == sum):
										pozycja = cordinate3[0] + window1[0], cordinate3[1] + window1[1]
										return pozycja
								else:
									numberOfCorrectBits = 0
									exitLoopBit = 1
									break
	return 0


def find_logo(botPosition,logo):
	box3 = logo.getbbox()
	img = ImageGrab.grab()
	screenSize = [0, 0, img.size[0], img.size[1]]
	screenSize=wedkarz.botWindowPosition(screenSize,botPosition,img)
	h = 0
	print(
		f"dla watku {threading.current_thread().name}  obszar poszukiwań: szerokosc: {screenSize[0]} {screenSize[2]} wysokosc: {screenSize[1]} {screenSize[3]}")
	for a in range(screenSize[0], (screenSize[2])):
		for b in range(screenSize[1], (screenSize[3])):
			cordinate2 = a, b
			cordinate1 = 0, 0
			if (img.getpixel(cordinate2)) == (logo.getpixel(cordinate1)):
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
							# print("blad zgodnosci pixela: ", h)
							h = 0
							break
	return 0

def numpyWhichNumber(sample, img):
	if sample.shape != img.shape:
		print("shape warning")
		print(sample.shape, img.shape)
		return 0
	# plt.imshow(img)
	# plt.show()
	# plt.imshow(sample)
	# plt.show()
	comparison = sample == img
	equal_arrays = comparison.all()
	if equal_arrays:
		return 1
	else:
		return 0



def numpyFinder(searchWindow, sample, filter):
	bounding_box = {'top': searchWindow[1], 'left': searchWindow[0], 'width': searchWindow[2] - searchWindow[0],
	                'height': searchWindow[3] - searchWindow[1]}
	sct_img = sct.grab(bounding_box)  # pobranie wycinka z monitora do buffora
	img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")  # tworzenie kopii wycinku z bufora
	# do podgladu wycinka przed zmiana
	# plt.imshow(img)
	# plt.show()
	color_filter_30 = np.array([0, 15, 255])  # Losowy kolor by w niego zmienic pixele nie majace znaczenia

	img = np.array(img)  # konwersja z wycinka obrazu z bufora  do tablicy numpy
	img[np.all(img != filter,
	           axis=-1)] = color_filter_30  # Dla wszystkich pixeli jezeli ktorykolwiek jest inny niz wazny zamien na taki sam kolor
	# do podgladu wycinka po zmianie
	# plt.imshow(img)
	# plt.show()
	# plt.imsave("plot\plot"+str(random.randint(1,100))+".png",img)
	# plt.imshow(sample)
	# plt.show()
	# szukanie ktory komunikat
	result = cv2.matchTemplate(img, sample, cv2.TM_SQDIFF_NORMED)  # wyszukiwanie obrazu w obrazie
	mn, _, mnLoc, maxLoc = cv2.minMaxLoc(result)  # wynik obrazu w obrazie (mn o ile odbiega od przykladu)
	# print(f"Podobienstwo :", maxLoc, mn, threading.current_thread().name)
	if mn < 0.1:
		# plt.imshow(img)
		# plt.show()
		# print(f"Podobienstwo :", maxLoc, mn, threading.current_thread().name)
		return (maxLoc, img)
	return (0, 0)

def numpyCloudFinder(searchWindow, sample, samplebase):
	bounding_box = {'top': searchWindow[1], 'left': searchWindow[0], 'width': searchWindow[2] - searchWindow[0],
	                'height': searchWindow[3] - searchWindow[1]}
	sct_img = sct.grab(bounding_box)  # pobranie wycinka z monitora do buffora
	img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")  # tworzenie kopii wycinku z bufora
	# do podgladu wycinka przed zmiana
	# plt.imshow(img)
	# plt.show()
	# color_filter_30 = np.array([0, 15, 255])  # Losowy kolor by w niego zmienic pixele nie majace znaczenia
	# img = np.array(img)  # konwersja z wycinka obrazu z bufora  do tablicy numpy
	# img[np.all(img != filter,
	#            axis=-1)] = color_filter_30  # Dla wszystkich pixeli jezeli ktorykolwiek jest inny niz wazny zamien na taki sam kolor
	# do podgladu wycinka po zmianie
	# plt.imshow(img)
	# plt.show()
	# plt.imsave("plot\plot"+str(random.randint(1,100))+".png",img)
	# plt.imshow(sample)
	# plt.show()
	# szukanie ktory komunikat
	result = cv2.matchTemplate(img, sample, cv2.TM_SQDIFF_NORMED)  # wyszukiwanie obrazu w obrazie
	mn, _, mnLoc, maxLoc = cv2.minMaxLoc(result)  # wynik obrazu w obrazie (mn o ile odbiega od przykladu)
	# print(f"Podobienstwo :", maxLoc, mn, threading.current_thread().name)
	if mn < 0.1:
		# plt.imshow(img)
		# plt.show()
		# print(f"Podobienstwo :", maxLoc, mn, threading.current_thread().name)
		return (maxLoc, img)
	return (0, 0)