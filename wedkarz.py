import os
import random
import time
from tkinter import *
import threading
import pyautogui
from PIL import ImageGrab, ImageDraw, Image
from enum import Enum
from queue import Queue
import data



# Wczytaj zdjęcia by operować nimi biblioteką PIL(funkcja szukajwoknie)
def load_images_toPIL(folder):
    images = {}
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder, filename))
        if img is not None:
            #print(filename)
            images[filename] = img
    return images


ryby = load_images_toPIL('img/ryby/')
sample = load_images_toPIL('img/samples/')
chat = load_images_toPIL('img/chat/')
queue = Queue()

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

pustybit = (0, 15, 255)

#GLOBAL VARIABLES
########################################################################
RESTART_COUNT = 0 #licznik ile razy boty łącznie zostaly zrestartowane podczas aktualneej sesji
THREAD = 1 # Zmienna do konczenia wszystkich watkow (STOP botow)

OPEN = data.DATA.get("Otwieraj_Ryby")
PRINTSCREEN = data.DATA.get("Zapis_Screenow")
REMOVE_TRASH = data.DATA.get("Usuwaj_Smieci")
RESOLUTION = data.DATA.get("Rozdzielczosc_Klienta") #1=640:360 / 800:600 rozdzielczość klienta



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
        screenSize[1] = int(img.size[1] / 2)
    elif botPosition == 2:
        screenSize[0] = int((img.size[0] / 2) + 1)
        screenSize[3] = int((img.size[1] / 2) + 1)
    elif botPosition == 3:
        screenSize[2] = int(img.size[0] / 2)
        screenSize[1] = int(img.size[1] / 2)
    elif botPosition == 4:
        screenSize[0] = int((img.size[0] / 2) + 1)
        screenSize[3] = int((img.size[1] / 2) + 1)
    h = 0
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


def czytajCHAT(oknoChatSTART, oknoChatEND):
    szukaj = szukajwoknie(oknoChatSTART, oknoChatEND, chat["lowienie.png"])
    if (szukaj == 0):
        print("szukam")
    else:
        print("ZNALEZIONO LOWIENIE")
        for x in range(1,6):
            if szukajwoknie(oknoChatSTART, oknoChatEND, chat[f"{x}.png"]) != 0:
                return x
    return 0



def spacje(ilosc, koordylowienia):
    time.sleep(0.1)
    pyautogui.moveTo(koordylowienia[0], koordylowienia[1], 0.1)
    for s in range(0, ilosc):
        r = (random.randint(1, 6)) / 100
        time.sleep(0.08 - r)
        pyautogui.click(button='right')


def start():
    global root
    global THREAD
    print("NAZWA BOTA: ",threading.current_thread().name)
    THREAD = 1
    start1()
    print("Koniec")

def startNewBots(numberOfBots:int):
    for botNumber in range(1,numberOfBots+1):
        thread = threading.Thread(target=start,name=BotPosition(botNumber).name)
        thread.start()





def usun(oknostart, okno, oknoeq1, oknoeq2):
    global INFO1
    global INFO2
    first = szukajwoknie(oknostart, okno, sample["kosz.png"])
    if first == 0:
        time.sleep(5)
        return 0
    move(first)
    second = szukajwoknie(oknostart, okno, sample["usun.png"])
    if second == 0:
        time.sleep(5)
        return 0
    border1 = second[0] - 50, second[1] - 215
    border2 = border1[0] + 170, border1[1] + 200

    for i in range(8):  # 0 - 7
        item1 = szukajwoknie(oknoeq1, oknoeq2, sample["pierscien.png"])
        if (item1 != 0):
            slot = szukajwoknie(border1, border2, sample["puste.png"])
            pyautogui.moveTo(item1[0], item1[1], 0.2)
            time.sleep(0.2)
            pyautogui.dragTo(slot[0], slot[1], 0.3)

        item2 = szukajwoknie(oknoeq1, oknoeq2, sample["plaszcz.png"])
        if (item2 != 0):
            print("plaszcz")
            slot = szukajwoknie(border1, border2, sample["puste.png"])
            pyautogui.moveTo(item2[0], item2[1], 0.2)
            time.sleep(0.2)
            pyautogui.dragTo(slot[0], slot[1], 0.3)

        if (item1 == 0):
            if (item2 == 0):
                move(first)
                return 1
        move(second)
    move(first)


def move(gdzie):
    pyautogui.moveTo(gdzie[0], gdzie[1], 0.2)
    time.sleep(0.3)
    pyautogui.click()


def start1():
    (oknostart1, okno1, oknoMaleS1, oknoMale1, oknoeqS1, oknoeq1, ekwipunek1) = checkboxy()
    sprawdzanie = 10
    global INFO1
    global INFO2
    global RESTART_COUNT
    koordyrobaka1 = szukajwoknie(oknostart1, okno1, sample["robak.png"])
    if (koordyrobaka1 == 0):
        print("Brak robaka")
        return 0
    # szukaj lowienia
    koordylowienia1 = szukajwoknie(oknostart1, okno1, sample["low.png"])
    if (koordylowienia1 == 0):
        print("brak lowienia")
        return 0
    print("ZNALEZIONO ROBAKA I LOWIENIE")
    while THREAD == 1:
        r1 = random.randint(1, 3) / 100
        r2 = random.randint(1, 3) / 100
        time.sleep(2)
        pyautogui.moveTo(koordyrobaka1[0], koordyrobaka1[1], 0.1)
        time.sleep(0.05)
        pyautogui.click(button='right')
        pyautogui.moveTo(koordylowienia1[0], koordylowienia1[1], 0.1)
        time.sleep(0.05)
        pyautogui.click(button='right')
        time.sleep(7)
        print()
        print("ilosc restartow: ", RESTART_COUNT)
        lowie1 = 0
        k = 0
        while (lowie1 == 0):
            lowie1 = szukajliczb(k, oknoMaleS1, oknoMale1)
            k = k + 1
            if (lowie1 == 7):
                RESTART_COUNT += 1
                time.sleep(4)
                start1()
            if (lowie1 > 0):
                sprawdzanie = sprawdzanie + 1
                spacje(lowie1, koordylowienia1)
                time.sleep(5)
                if OPEN == 1:
                    otwieranie(oknoeqS1, oknoeq1, sprawdzanie)
                if (sprawdzanie > 45):
                    sprawdzanie = 1
                    if REMOVE_TRASH == 1:
                        usun(oknostart1, okno1, oknoeqS1, oknoeq1)
    return 0


def szukajliczb(k, oknoCHAT1, oknoCHAT2):
    # ilosc  prob przed restartem
    if (k > 800):
        return 7
    else:
        wynik = czytajCHAT(oknoCHAT1, oknoCHAT2)
    return wynik


def otwieranie(oknoeq1, oknoeq2, sprawdzanie):
    pyautogui.moveTo(oknoeq1[0], oknoeq1[1], 0.1)
    if (sprawdzanie == 45):
        for s in range(0, 9):
            pyautogui.moveTo(oknoeq1[0] + 165, 5 + (oknoeq1[1] + (s * 32)), 1)
            pyautogui.moveTo(oknoeq1[0] + 0, 5 + (oknoeq1[1] + (s * 32)), 1)

    if sprawdzanie % 6 == 3:
        for key in ryby:
            ryba = szukajwoknie(oknoeq1, oknoeq2, ryby[key])
            if (ryba != 0):
                pyautogui.moveTo(ryba[0], ryba[1], 0.25)
                time.sleep(0.35)
                pyautogui.click(button='right')


# MENU


def stop():
    global THREAD
    THREAD = 0


def checkboxy():
    global INFO1
    global INFO2
    threadName=str(threading.current_thread().name)
    threadValue = 0
    if threadName == "TOP_LEFT":
        threadValue = 1
    elif threadName == "TOP_RIGHT":
        threadValue = 2
    elif threadName == "BOTTOM_LEFT":
        threadValue = 3
    elif threadName == "BOTTOM_RIGHT":
        threadValue = 4
    else:
        print("Cos poszlo nie tak :(")

    koordyLoga1 = find_logo(threadValue)
    if koordyLoga1 == 0:
        print("BRAK LOGA W WATKU ",threading.current_thread().name)


    # OKNO1
    oknostart1 = koordyLoga1
    if RESOLUTION==1:
        okno1 = oknostart1[0] + 640, oknostart1[1] + 400
    else:
        okno1 = oknostart1[0] + 800, oknostart1[1] + 600
    ekipunek1 = szukajwoknie(oknostart1, okno1, sample["eq.png"])

    if (ekipunek1 == 0):
        print("nie znaleziono ekwipunku w watku ",threading.current_thread().name)
    else:
        # pozycja wzgledem probki
        oknoeqS1 = ekipunek1[0] + 15, ekipunek1[1] - 70
        # rozmiar
        oknoeq1 = oknoeqS1[0] + 165, oknoeqS1[1] + 295

    chat1 = szukajwoknie(oknostart1, okno1, sample["chat.png"])
    if (chat1 == 0):
        print("nie znaleziono CHATU w watku",threading.current_thread().name)
    else:
        # pozycja wzgledem probki
        oknoCHATS1 = chat1[0] - 480, chat1[1] - 30
        # rozmiar
        oknoCHAT1 = oknoCHATS1[0] + 450, oknoCHATS1[1] + 20


    if PRINTSCREEN == 1:
        img = ImageGrab.grab(bbox=None)
        draw = ImageDraw.Draw(img)
        rysujokno1 = oknostart1 + okno1
        rysujeq1 = oknoeqS1 + oknoeq1
        rysujchat1 = oknoCHATS1 + oknoCHAT1
        boxS = oknoeqS1[0] + 16, oknoeqS1[1] + 14
        boxE = oknoeqS1[0] + 24, oknoeqS1[1] + 20
        rysujDebugg = boxS + boxE
        # rysowanie
        draw.rectangle(rysujokno1, outline=128, width=3)
        draw.rectangle(rysujeq1, outline=(64, 255, 128), width=3)
        draw.rectangle(rysujchat1, outline=(0, 255, 255), width=3)
        draw.rectangle(rysujDebugg, outline=(128, 255, 96), width=1)
        img.save("boxy.png")
        time.sleep(0.5)

    ##DODAC
    return (oknostart1, okno1, oknoCHATS1, oknoCHAT1, oknoeqS1, oknoeq1, ekipunek1)


