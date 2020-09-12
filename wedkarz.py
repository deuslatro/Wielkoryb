import time
import os
import random
import pyautogui
from tkinter import *
from PIL import ImageGrab, ImageDraw, Image


#Wczytaj zdjęcia by operować nimi biblioteką PIL(funkcja szukajwoknie)
def load_images_toPIL(folder):
    images = {}
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder,filename))
        if img is not None:
            print(filename)
            images[filename] = img
    return images


ryby = load_images_toPIL('img/ryby/')
sample = load_images_toPIL('img/samples/')
chat = load_images_toPIL('img/chat/')

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

pustybit = (0, 15, 255)
bialybit = (255, 255, 255)
bitchatu = (255 , 230, 186)

########################################################################
# zmienne Globalne
RESTART = 0
DEBUGGER = 0
STAN = 1
OTW = 0
MULTI = 0
INFO1 = StringVar
INFO2 = StringVar
ZAPIS = 0
USUN = 0
root = Tk()
debug = Tk()
debug.withdraw()

KLIENT1 = 0

def szukajloga(ktore):
    logo = sample["logo.png"]
    box3 = logo.getbbox()
    img = ImageGrab.grab()
    koordyEkranu = [0, 0, img.size[0], img.size[1]]
    print(img.size[0]/2)
    if (MULTI == 1):
        if (ktore == 1):
            koordyEkranu[2] = int(img.size[0]/2)
        elif (ktore == 2):
            koordyEkranu[0] = int((img.size[0]/2)+1)
    h = 0
    for a in range(koordyEkranu[0], (koordyEkranu[2])):
        for b in range(0, (koordyEkranu[3])):
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
                                cordinate4 = cordinate3
                                print("znaleziono Logo gry")
                                return cordinate4
                        else:
                            print("blad zgodnosci pixela: ", h)
                            h = 0
                            break
    return 0

#szuka danej bitmapy w danym obszarze i zwraca jej prawy dolny(?) rog jako koordynaty [uwzglednia maske (pusty bit)]
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
                #print(f'perwszy bit zgodny w:    :   {szukany.filename}')
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
                            if (szukany.getpixel(cordinate1) == pustybit):
                                #print("pusty")
                                h = h + 1
                                continue
                            else:
                                #print("zgodny",szukany.filename)
                                if cordinate3[0] >= szer or cordinate3[1] >= wys:
                                    h = 0
                                    a = 1
                                    #print("POZA INDEKSEM")
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




def czytajCHAT(oknoChatSTART,oknoChatEND):
    szukaj=szukajwoknie(oknoChatSTART,oknoChatEND,chat["lowienie.png"])
    if(szukaj==0):
        print("szukam")
    else:
        print("ZNALEZIONO LOWIENIE")
        if(szukajwoknie(oknoChatSTART,oknoChatEND,chat["1.png"])!=0):
            return 1
        else:
            if (szukajwoknie(oknoChatSTART, oknoChatEND, chat["2.png"]) != 0):
                return 2
            else:
                if (szukajwoknie(oknoChatSTART, oknoChatEND, chat["3.png"]) != 0):
                    return 3
                else:
                    if (szukajwoknie(oknoChatSTART, oknoChatEND, chat["4.png"]) != 0):
                        return 4
                    else:
                        if (szukajwoknie(oknoChatSTART, oknoChatEND, chat["5.png"]) != 0):
                            return 5
    return 0





def debugger():
    global DEBUGGER
    global debug
    global MULTI
    if DEBUGGER == 0:
        if MULTI == 1:
            print("wylacz MULTIKLIENTA by debugowac")
        DEBUGGER = 1
        debug.deiconify()
        print("DEBUG MODE ON")
    else:
        if DEBUGGER == 1:
            DEBUGGER = 0
            debug.withdraw()


def test2():
    print("test2DEBUG")
    (oknostart1, okno1, oknoChatSTART, oknoChatEND, oknoeqS1, oknoeq1, ekipunek1) = checkboxy()
    szukaj = szukajwoknie(oknoChatSTART, oknoChatEND, chat["test.png"])
    if (szukaj == 0):
        print("szukam")
    else:
        print("ZNALEZIONO GRATUUUUUUUUULACJE")
        print("ZNALEZIONO GRATUUUUUUUUULACJE")
        print("ZNALEZIONO GRATUUUUUUUUULACJE")
        print("ZNALEZIONO GRATUUUUUUUUULACJE")
        print("ZNALEZIONO GRATUUUUUUUUULACJE")
        print("ZNALEZIONO GRATUUUUUUUUULACJE")




    DEBUGGER = 0
    debug.protocol('WM_DELETE_WINDOW', debug.withdraw)
    debug.withdraw()
    debug.mainloop()


def probka(a):
    (oknostart1, okno1, oknoCHATS1, oknoCHAT1, oknoeqS1, oknoeq1, ekipunek1) = checkboxy()
    #Obszar pobierania próbki(można sprawdzić go checkboxem)
    boxS = oknoeqS1[0] + 16, oknoeqS1[1] + 14
    boxE = oknoeqS1[0] + 24, oknoeqS1[1] + 20
    img = ImageGrab.grab(bbox=boxS + boxE)
    print("pobieram probke:", a)
    for key in ryby:
        if(a==key):
            boxWS = oknostart1[0] + 560, oknostart1[1] + 580
            boxWE = oknostart1[0] + 570, oknostart1[1] + 600
            img = ImageGrab.grab(bbox=boxWS + boxWE)
            img.save(f"img/ryby/{key}")
            ryby[key]=img
    for key in sample:
        if(a=="lowienie.png"):
            img.save(f"img/samples/{key}")
            sample[key] = img
        elif(a==key):
            img.save(f"img/samples/{key}")
            sample[key]=img
    print(f'Zmieniono {a}')






def spacje(ilosc, koordylowienia):
    time.sleep(0.1)
    pyautogui.moveTo(koordylowienia[0], koordylowienia[1], 0.1)
    for s in range(0, ilosc):
        r = (random.randint(1, 6)) / 100
        time.sleep(0.08 - r)
        pyautogui.click(button='right')




def start():
    global MULTI
    global root
    global KLIENT1
    KLIENT1 = 1
    if (MULTI == 0):
        start1()
        print("Koniec")


def usun(oknostart, okno, oknoeq1, oknoeq2):
    global INFO1
    global INFO2
    INFO1.set("usuwanie śmieci...")
    INFO2.set("usuwanie śmieci...")
    Tk.update(root)

    first = szukajwoknie(oknostart, okno, sample["kosz.png"])
    if first == 0:
        INFO1.set("okno usuwania")
        INFO2.set("jest nieosiagalne")
        Tk.update(root)
        time.sleep(5)
        return 0
    move(first)
    second = szukajwoknie(oknostart, okno, sample["usun.png"])
    if second == 0:
        INFO1.set("przycisk usuwania")
        INFO2.set("jest nieosiągalny")
        Tk.update(root)
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
    global RESTART
    koordyrobaka1 = szukajwoknie(oknostart1, okno1, sample["robak.png"])
    if (koordyrobaka1 == 0):
        return 0
    # szukaj lowienia
    koordylowienia1 = szukajwoknie(oknostart1, okno1, sample["low.png"])
    if (koordylowienia1 == 0):
        return 0
    while KLIENT1 == 1:
        r1 = random.randint(1, 3) / 100
        r2 = random.randint(1, 3) / 100
        time.sleep(2)
        pyautogui.moveTo(koordyrobaka1[0], koordyrobaka1[1], 0.2)
        time.sleep(0.3 + r1)
        pyautogui.click(button='right')
        pyautogui.moveTo(koordylowienia1[0], koordylowienia1[1], 0.2)
        time.sleep(0.3 + r1 - r2)
        pyautogui.click(button='right')
        time.sleep(7)
        print()
        print("ilosc restartow: ", RESTART)
        lowie1 = 0
        k = 0
        while (lowie1 == 0):
            lowie1 = szukajliczb(k, oknoMaleS1, oknoMale1)
            k = k + 1
            if (lowie1 == 7):
                RESTART += 1
                time.sleep(4)
                start1()
            if (lowie1 > 0):
                sprawdzanie = sprawdzanie + 1
                spacje(lowie1, koordylowienia1)
                time.sleep(5)
                if OTW == 1:
                    otwieranie(oknoeqS1, oknoeq1, sprawdzanie)
                    if (sprawdzanie > 45):
                        sprawdzanie = 1
                        if USUN == 1:
                            usun(oknostart1, okno1, oknoeqS1, oknoeq1)
    return 0





def szukajliczb(k, oknoCHAT1, oknoCHAT2):
    # ilosc  prob przed restartem
    if MULTI == 1:
        if (k > 800):
            return 7
    # ustalenie po ilu powtórzeniach restart
        if (k > 1100):
            return 7
        return 0
    else:
        wynik=czytajCHAT(oknoCHAT1,oknoCHAT2)
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
    global KLIENT1
    KLIENT1 = 0

def checkboxy():
    global INFO1
    global INFO2
    #INFO1.set("TEST checkboxow")
    if MULTI == 1:
        print("TEST checkboxow")

    koordyLoga1 = szukajloga(1)
    if (koordyLoga1 == 0):
        print("nie znaleziono loga gry")
        print("Brak Loga po lewej stronie ekranu")
        return 2  # 2 brak loga

    if (MULTI == 1):
        koordyLoga2 = szukajloga(2)
        if (koordyLoga2 == 0):
            print("nie znaleziono loga gry")
            print("Brak Loga po prawej stronie ekranu")
            return 2

    # OKNO1
    oknostart1 = koordyLoga1
    okno1 = oknostart1[0] + 780, oknostart1[1] + 610
    ekipunek1 = szukajwoknie(oknostart1, okno1, sample["eq.png"])

    if (ekipunek1 == 0):
        print("nie znaleziono ekwipunku w 1 kliencie")
    else:
        #pozycja wzgledem probki
        oknoeqS1 = ekipunek1[0] + 15, ekipunek1[1] - 70
        #rozmiar
        oknoeq1 = oknoeqS1[0] + 165, oknoeqS1[1] + 295

    chat1 = szukajwoknie(oknostart1,okno1,sample["chat.png"])
    if(chat1 == 0):
        print("nie znaleziono CHATU w 1 kliencie")
    else:
        # pozycja wzgledem probki
        oknoCHATS1 = chat1[0] - 480, chat1[1] - 30
        # rozmiar
        oknoCHAT1 = oknoCHATS1[0] + 450, oknoCHATS1[1] + 20


    # OKNO2
    if (MULTI == 1):
        oknostart2 = koordyLoga2
        okno2 = oknostart2[0] + 780, oknostart2[1] + 610
        ekipunek2 = szukajwoknie(oknostart2, okno2, sample["eq.png"])
        if (ekipunek2 == 0):
            print("nie znaleziono ekwipunku w 2 kliencie")
        oknoeqS2 = ekipunek2[0] + 15, ekipunek2[1] - 70
        oknoeq2 = oknoeqS2[0] + 165, oknoeqS2[1] + 295

    if ZAPIS == 1:
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

        if (MULTI == 1):
            rysujokno2 = oknostart2 + okno2
            rysujeq2 = oknoeqS2 + oknoeq2
            # rysowanie
            draw.rectangle(rysujokno2, outline=128, width=3)
            draw.rectangle(rysujeq2, outline=(64, 255, 128), width=3)
        img.save("boxy.png")
        time.sleep(0.5)

    ##DODAC
    if MULTI == 1:
        return (oknostart1, okno1,oknoCHATS1, oknoCHAT1 , oknoeqS1, oknoeq1, ekipunek1, oknostart2, okno2,
                 oknoeqS2, oknoeq2, ekipunek2)
    if MULTI == 0:
        return (oknostart1, okno1,oknoCHATS1, oknoCHAT1 , oknoeqS1, oknoeq1, ekipunek1)


def otw():
    global OTW
    if OTW == 0:
        OTW = 1
    else:
        OTW = 0


def mlt():
    global MULTI
    if MULTI == 0:
        MULTI = 1
    else:
        MULTI = 0


def zap():
    global ZAPIS
    if ZAPIS == 0:
        ZAPIS = 1
    else:
        ZAPIS = 0


def usu():
    global USUN
    if USUN == 0:
        USUN = 1
    else:
        USUN = 0


if __name__ == '__main__':
    print("Otwórz przez menu (okno.py)")

def test():
    print("TEST")
    time.sleep(5)
    print("ESSA")