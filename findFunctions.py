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


def find_logo(botPosition, logo):
	box3 = logo.getbbox()
	img = ImageGrab.grab()
	screenSize = [0, 0, img.size[0], img.size[1]]
	screenSize = wedkarz.botWindowPosition(screenSize, botPosition, img)
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


def numpySameFinder(img, sample, filter):
	"""
	Takes 2 images and compare them using numpy
	if they are the same return 1 else return 0
	:param img: numpy Array OR tuple with all corners of the image position from screen
	:param sample: numpy array of the sample
	:param filter: numpy 1:3 array if we wanna use filter otherwise can be any
	:return: 1 SAME 0 DIFFRENT
	"""
	if type(img) is tuple:
		bounding_box = {'top': img[1], 'left': img[0], 'width': img[2] - img[0],
		                'height': img[3] - img[1]}
		sct_img = sct.grab(bounding_box)  # pobranie wycinka z monitora do buffora
		img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")  # tworzenie kopii wycinku z bufora
		img = np.array(img)  # konwersja z wycinka obrazu z bufora  do tablicy numpy
	if sample.shape != img.shape:
		print("shape warning")
		print(sample.shape, img.shape)
		return 0
	color_filter_30 = np.array([0, 15, 255])  # Losowy kolor by w niego zmienic pixele nie majace znaczenia
	if type(filter) == type(color_filter_30):
		img[np.all(img != filter,
		           axis=-1)] = color_filter_30  # Dla wszystkich pixeli jezeli ktorykolwiek jest inny niz wazny zamien na taki sam kolor
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


def takeSample(searchWindow, filename, filter):
	bounding_box = {'top': searchWindow[1], 'left': searchWindow[0], 'width': searchWindow[2] - searchWindow[0],
	                'height': searchWindow[3] - searchWindow[1]}
	sct_img = sct.grab(bounding_box)  # pobranie wycinka z monitora do buffora
	img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")  # tworzenie kopii wycinku z bufora
	img = np.array(img)  # konwersja z wycinka obrazu z bufora  do tablicy numpy
	if filter != 1:
		color_filter_30 = np.array([0, 15, 255])  # Losowy kolor by w niego zmienic pixele nie majace znaczenia
		img[np.all(img != wedkarz.color_filter_20,
		           axis=-1)] = color_filter_30  # Dla wszystkich pixeli jezeli ktorykolwiek jest inny niz wazny zamien na taki sam kolor

	plt.imsave("img\debugger\sample\\" + filename + ".png", img)
	return 0


def numpySimilarFinder(searchWindow, sample, similarity):
	"""
	Takes part of screen and try to find sample image inside it
	:param searchWindow: tuple with all corners of screen you wanna search
	:param sample: numpy array of the sample
	:param similarity: 0-1 value how much sample was detected by search algorytm
	:return: sample location,array of searched screen similarity threshold met |  0,0 threshold not met
	"""
	if isinstance(searchWindow, (np.ndarray)):
		img = searchWindow
	else:
		bounding_box = {'top': searchWindow[1], 'left': searchWindow[0], 'width': searchWindow[2] - searchWindow[0],
		                'height': searchWindow[3] - searchWindow[1]}
		sct_img = sct.grab(bounding_box)  # pobranie wycinka z monitora do buffora
		img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")  # tworzenie kopii wycinku z bufora
		img = np.array(img)  # konwersja z wycinka obrazu z bufora  do tablicy numpy
	result = cv2.matchTemplate(img, sample, cv2.TM_SQDIFF_NORMED)  # wyszukiwanie obrazu w obrazie
	mn, x, mnLoc, maxLoc = cv2.minMaxLoc(result)  # wynik obrazu w obrazie (mn o ile odbiega od przykladu)
	if mn < similarity:
		# plt.imshow(img)
		# plt.show()
		# print(f"Podobienstwo :", 1-mn, threading.current_thread().name)
		# plt.imsave('datasets\Images\Samples\\'+ str(mn) + '.png', img)
		return (img, 1 - mn)

	return (0, 0)


def numpyFindWindowInArray(array, size, similarity):
	"""
	This function search for "window" in image
	it sums rows value in turn and compare them in pairs
	if absolute value of subbtract of 2 rows is bigger than treshold
	then it resize array into smaller one
	:param array:
	:param position:
	:param size:
	:param similarity:
	:return:
	"""
	x = np.shape(array)
	# print(similarity)
	# print(x)
	TMParray = array[:, :, :]
	xline=[]
	yline=[]

	for i in range(0,x[1]-1):
		x1=TMParray[:,i,:].sum(dtype=int)
		x2=TMParray[:,i+1,:].sum(dtype=int)
		x3=x1-x2
		if abs(x3) >= 5000:
			xline.append(i)
			# print(i,':',x1,x2,'abs',abs(x3),'x3',x3)

	if len(xline)<2:
		return TMParray
	width = xline[-1]-xline[0] + 2
	# print(xline)
	# print('last',xline[-1])
	# print('szer',width)
	height = np.round(width*0.7)
	# print('wys',height)
	TMParray = array[:, xline[0]:xline[0]+width, :]
	# print(np.shape(TMParray))

	for i in range(0,x[0]-1):
		x1=TMParray[i,:,:].sum(dtype=int)
		x2=TMParray[i+1,:,:].sum(dtype=int)
		x3=x1-x2
		if abs(x3) >= 3500:
			# print(x3)
			yline.append(i)
			# print(i,':',x1,x2,'abs',abs(x3),'x3',x3)
			break

	# print(yline)
	# print(height)
	TMParray = TMParray[yline[0]:yline[0]+int(height),:, :]
	# plt.imsave("img\debugger\sample\\" + str(similarity) + ".png", TMParray)
	# print(np.shape(TMParray))
	# plt.imshow(TMParray)
	# plt.show()
	return TMParray
