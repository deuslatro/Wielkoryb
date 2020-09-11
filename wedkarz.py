import time
import os
import random
import numpy
import pyautogui
import PIL
from tkinter import *
from PIL import ImageGrab, ImageDraw, Image
import cv2




# Grafik do słowników (key to nazwa pliku) przykladowa petla zerujaca słownik:
#  for key in liczby:
#       liczby[key] = 0

#Wczytaj zdjęcia by operować nimi biblioteką PIL(funkcja szukajwoknie)
def load_images_toPIL(folder):
    images = {}
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder,filename))
        if img is not None:
            print(filename)
            images[filename] = img
    return images

#Wczytaj zdjęcia by operować nimi w cv2(funkcje activeseartch,find_numbers etc)
def load_images_tocv2(folder):
    images = {}
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            print(filename)
            images[filename] = img
    return images

liczby = load_images_tocv2('img/liczby/')
ryby = load_images_toPIL('img/ryby/')
sample = load_images_toPIL('img/samples/')
czerwoneokno = cv2.imread('img/CV2/okno.png')

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
                                h = h + 1
                                continue
                            else:
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

def active_search(sample, image):
    # pobiera wycinek ze screena i porownuje do duzej probki z folderu
    method = cv2.TM_SQDIFF_NORMED
    small_image = sample
    large_image = image
    # zastosowanie metody by poznac"granice"
    result = cv2.matchTemplate(small_image, large_image, method)
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)
    # Draw the rectangle:
    # koordynaty najlepszego znaleziska
    MPx, MPy = mnLoc
    # Step 2: Get the size of the template. This is the same size as the match.
    trows, tcols = small_image.shape[:2]
    # Przyciecie obrazka do najbardziej dopasowanego
    large_image = large_image[MPy:MPy + trows, MPx:MPx + tcols]
    # tylko jezeli blad jest maly(wykryto czerwone okienko)
    if (mn < 0.25):
        # zwraca tylko czerwone okno
        return large_image
    else:
        # zwraca 0 co ponowi próbe
        return 0


def which_number(sample, image):
    # pobiera czerwone okno z liczba i porownuje do malej probki z folderu
    method = cv2.TM_SQDIFF_NORMED
    small_image = sample
    large_image = image
    # zastosowanie metody by poznac"granice"
    result = cv2.matchTemplate(small_image, large_image, method)
    mn, _, mnLoc, _ = cv2.minMaxLoc(result)
    # zwroc 1 jezeli maly blad(znaleziono)
    # zwroc 0 jezeli ma szukac dalej
    # tylko jezeli blad jest maly
    if (mn < 0.05):
        print("mn = ", mn)
        return 0
    else:
        return mn


def main():
    print("wczytywanie menu")
    menu()


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
    for key in ryby:
        print(f'RYBA    :   {key}')
        print(ryby[key])


def debuguj():
    global DEBUGGER
    global debug
    OPTIONS = [
        "robak.png",
        "lowienie.png",
        "ryba1.png",
        "ryba2.png",
        "ryba3.png",
        "ryba4.png",
        "ryba5.png",
        "ryba6.png",
        "ryba7.png",
        "ryba8.png",
        "ryba9.png",
        "ryba10.png",
        "ryba11.png",
        "ryba12.png",
        "plaszcz.png",
        "pierscien.png",
        "puste.png",
        "test.png"
    ]
    variable = StringVar(debug)
    variable.set(OPTIONS[0])
    w = OptionMenu(debug, variable, *OPTIONS)
    w.pack()
    debug.title("DEBUGGER v3.1")
    kolor = "gray"
    leftFrame = Frame(debug, bg=kolor)
    leftFrame.pack(side=LEFT)
    rightFrame = Frame(debug)
    rightFrame.pack(side=LEFT)
    middleFrame = Frame(debug, bg=kolor)
    middleFrame.pack(side=LEFT)
    buttons = Button(debug, text="PODMIEN", fg="red", command=lambda: probka(variable.get()))
    buttons.pack()
    button5 = Button(debug, text="TEST2", fg="red", command=test2)
    button5.pack()
    label0 = Label(debug, fg="red", text="1.Wyłącz MultiClient przed debugowaniem")
    label0.pack()
    label1 = Label(debug, fg="red",text="2.Pobierz i nadpisz próbke danego przedmiotu z pierwszego slota EQ/ ikonke lowienia z F4")
    label1.pack()
    label2 = Label(debug, fg="red", text="3.Zaznacz ZapisPNG i zrób Checkboxy a zobaczysz obszar jaki kopiuje debugger(najmniejszy kwadracik)")
    label2.pack()
    label3 = Label(debug, fg="red", text="OPIS POWSZECHNYCH PROBLEMÓW")
    label3.pack()
    label6 = Label(debug, text="Nie wykryto loga - Sprawdz czy w folderze jest dobrze wykonana próbka logo.png", fg="red")
    label6.pack(side=TOP)
    label7 = Label(debug,text="Jeżeli nie masz pewności co do próbki zrób PRINTSCREEN i zastęp próbke swoim wycinkiem", fg="red")
    label7.pack(side=TOP)
    label8 = Label(debug, text="Nie wykryto robaka / wędki (jak up tylko można naprawić debuggerem)", fg="red")
    label8.pack(side=TOP)
    label9 = Label(debug, text="Rusza myszką ale nie klika - URUCHOM JAKO ADMINISTRATOR", fg="red")
    label9.pack(side=TOP)
    label10 = Label(debug,text="Klika na coś inne niż robak(zdebuguj robaka z 1 slota eq)", fg="red")
    label10.pack(side=TOP)
    label11 = Label(debug, text="Inne Problemy można zgłaszać na adres: www.xd@xd.pl", fg="red")
    label11.pack(side=TOP)


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



def screen():
    print("printscreen")
    PIL.ImageGrab.grab(bbox=None)
    img = ImageGrab.grab()
    img.save("screen.png")


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
    if (MULTI == 1):
        start2()
    if (MULTI == 0):
        start1()


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
    (oknostart1, okno1, oknoCHATS1, oknoCHAT1, oknoeqS1, oknoeq1, ekwipunek1) = checkboxy()
    sprawdzanie = 10
    global INFO1
    global INFO2
    global RESTART
    INFO1.set("STARTOWANIE")
    INFO2.set("NIEAKTYWNY")
    Tk.update(root)
    koordyrobaka1 = szukajwoknie(oknostart1, okno1, sample["robak.png"])
    if (koordyrobaka1 == 0):
        INFO1.set("nie odnaleziono robaka")
        Tk.update(root)
        return 0
    # szukaj lowienia
    koordylowienia1 = szukajwoknie(oknostart1, okno1, sample["low.png"])
    if (koordylowienia1 == 0):
        INFO1.set("nie odnaleziono wedki")
        Tk.update(root)
        return 0
    status = 1
    while status == 1:
        r1 = random.randint(1, 3) / 100
        r2 = random.randint(1, 3) / 100
        time.sleep(3)

        pyautogui.moveTo(koordyrobaka1[0], koordyrobaka1[1], 0.2)
        time.sleep(0.3 + r1)
        pyautogui.click(button='right')
        pyautogui.moveTo(koordylowienia1[0], koordylowienia1[1], 0.2)
        time.sleep(0.3 + r1 - r2)
        pyautogui.click(button='right')

        INFO1.set("łowienie...")
        Tk.update(root)
        time.sleep(7)
        INFO1.set("szukanie...")
        Tk.update(root)
        print()
        print("ilosc restartow: ", RESTART)
        lowie1 = 0
        k = 0
        while (lowie1 == 0):
            lowie1 = szukajliczb(k, oknoMaleS1, oknoMale1)
            k = k + 1
            if (lowie1 == 7):
                RESTART += 1
                INFO1.set("Restart...")
                Tk.update(root)
                time.sleep(4)
                start1()
            if (lowie1 > 0):
                INFO1.set("WYŁAWIANIE")
                Tk.update(root)
                sprawdzanie = sprawdzanie + 1
                spacje(lowie1, koordylowienia1)
                time.sleep(5)
                if OTW == 1:
                    INFO1.set("OTWIERANIE")
                    Tk.update(root)
                    otwieranie(oknoeqS1, oknoeq1, sprawdzanie)
                    if (sprawdzanie > 45):
                        sprawdzanie = 1
                        if USUN == 1:
                            usun(oknostart1, okno1, oknoeqS1, oknoeq1)


def start2():
    (oknostart1, okno1, oknoCHATS1, oknoCHAT1, oknoeqS1, oknoeq1, ekipunek1, oknostart2, okno2, oknoCHATS2, oknoCHAT2,
     oknoeqS2, oknoeq2, ekwipunek2) = checkboxy()

    sprawdzanie = 10
    global INFO1
    global INFO2
    global RESTART
    INFO1.set("STARTOWANIE")
    INFO2.set("STARTOWANIE")
    Tk.update(root)

    koordyrobaka1 = szukajwoknie(oknostart1, okno1, sample["robak.png"])
    if (koordyrobaka1 == 0):
        INFO1.set("nie odnaleziono robaka")
        return 0
    koordylowienia1 = szukajwoknie(oknostart1, okno1, sample["low.png"])
    if (koordylowienia1 == 0):
        INFO1.set("nie odnaleziono wedki")
        return 0

    koordyrobaka2 = szukajwoknie(oknostart2, okno2, sample["robak.png"])
    if (koordyrobaka2 == 0):
        INFO2.set("nie odnaleziono robaka")
        return 0
    koordylowienia2 = szukajwoknie(oknostart2, okno2, sample["low.png"])
    if (koordylowienia2 == 0):
        INFO2.set("nie odnaleziono wedki")
        return 0

    status = 1
    while status == 1:
        time.sleep(3.5)
        INFO1.set("łowienie...")
        INFO2.set("łowienie...")
        Tk.update(root)

        print()
        print("ilosc restartow: ", RESTART)
        pyautogui.moveTo(koordyrobaka1[0], koordyrobaka1[1], 0.2)
        time.sleep(0.2)
        pyautogui.click(button='right')
        pyautogui.moveTo(koordylowienia1[0], koordylowienia1[1], 0.2)
        time.sleep(0.2)
        pyautogui.click(button='right')

        pyautogui.moveTo(koordyrobaka2[0], koordyrobaka2[1], 0.2)
        time.sleep(0.2)
        pyautogui.click(button='right')
        pyautogui.moveTo(koordylowienia2[0], koordylowienia2[1], 0.2)
        time.sleep(0.2)
        pyautogui.click(button='right')

        time.sleep(7)
        INFO1.set("szukanie...")
        INFO2.set("szukanie...")
        Tk.update(root)
        koniec = 0
        lowie1 = 0
        lowie2 = 0
        k = 0
        while (koniec == 0):
            if (lowie1 == 0):
                lowie1 = szukajliczb(k, oknoMaleS1, oknoMale1)
            if (lowie2 == 0):
                lowie2 = szukajliczb(k, oknoMaleS2, oknoMale2)
            k = k + 1
            if (lowie1 == 7):
                print("restart")
                INFO1.set("Restart...")
                Tk.update(root)
                RESTART += 1
                time.sleep(4)
                start2()
            if (lowie2 == 7):
                print("restart")
                INFO2.set("Restart...")
                Tk.update(root)
                RESTART += 1
                time.sleep(4)
                start2()

            if (lowie1 > 0):
                if (lowie1 != 9):
                    spacje(lowie1, koordylowienia1)
                    INFO1.set("WYŁOWIONA")
                    Tk.update(root)
                    lowie1 = 9

            if (lowie2 > 0):
                if (lowie2 != 9):
                    spacje(lowie2, koordylowienia2)
                    INFO1.set("WYŁOWIONA")
                    Tk.update(root)
                    lowie2 = 9

            if (lowie1 == 9):
                if (lowie2 == 9):
                    time.sleep(2)
                    if OTW == 1:
                        INFO1.set("OTWIERANIE")
                        INFO2.set("OTWIERANIE")
                        Tk.update(root)
                        sprawdzanie = sprawdzanie + 1
                        otwieranie(oknoeqS1, oknoeq1, sprawdzanie)
                        otwieranie(oknoeqS2, oknoeq2, sprawdzanie)
                    if (sprawdzanie > 45):
                        if USUN == 1:
                            usun(oknostart1, okno1, oknoeqS1, oknoeq1)
                            usun(oknostart2, okno2, oknoeqS2, oknoeq2)
                        sprawdzanie = 0
                    time.sleep(3)
                    koniec = 1


def szukajliczb(k, oknoMale1, oknoMale2):
    img = ImageGrab.grab(bbox=oknoMale1 + oknoMale2)
    image = numpy.array(img)
    # Convert RGB to BGR
    image = image[:, :, ::-1].copy()
    probability = []
    szukane = active_search(czerwoneokno, image)
    if isinstance(szukane, int):
        # ilosc  prob przed restartem
        if MULTI == 1:
            if (k > 800):
                return 7
        # ustalenie po ilu powtórzeniach restart
        if (k > 1100):
            return 7
        return 0
    else:
        print("wyskoczylo okno")
        i = 0

        szukaneWys=szukane.shape[0]
        for key in liczby:

            # zabezpieczenie wysokości ( dobra strone warunek? xD)
            if szukaneWys < liczby[key].shape[0]:
                print("pobrano za mala probke by uniknac bledu 'znajduje' 4")
                return 4

            # print("sprawdzam liczbe o indeksie",i)
            probability.append(which_number(liczby[key], szukane))
            if (probability[i] == 0):
                print("znaleziono", key)
                return (i + 1)
            i = i + 1
            # print("szansa",i," = ",probability[i])

        print("nie rozpoznano liczby w oknie, utworzono zrzut wykrycia")
        cv2.imwrite("zrzut.png", szukane)
        # zwraca indeks przykladu ktory byl najpodobniejszy do sprawdzanego
        print("droga eliminacji otrzumano liczbe", probability.index(min(probability)) + 1)
        return probability.index(min(probability)) + 1
    return 0


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
def menu():
    global INFO1
    global INFO2
    global root
    # root = Tk()
    root.title("Wielkoryb v.1.8")
    kolor = "snow3"
    leftFrame = Frame(root, bg=kolor)
    leftFrame.pack(side=LEFT)
    rightFrame = Frame(root)
    rightFrame.pack(side=LEFT)
    middleFrame = Frame(root, bg=kolor)
    middleFrame.pack(side=LEFT)
    INFO1 = StringVar()
    INFO1.set("NIEAKTYWNY")
    INFO2 = StringVar()
    INFO2.set("NIEAKTYWNY")
    label1 = Label(leftFrame, text="Wielkoryb v.1.7", fg="red", bg=kolor,font=10)
    label2 = Label(leftFrame, text="Wystartuj Bota", fg="cyan", bg=kolor)
    label6 = Label(leftFrame, text="DEBUGGER", fg="cyan", bg="red")
    label3 = Label(leftFrame, text="CheckBox", fg="cyan", bg=kolor)
    label5 = Label(leftFrame, text="Wyjscie", fg="cyan", bg=kolor)
    label4 = Label(leftFrame, text="PRINTSCREEN", fg="cyan", bg=kolor)

    button1 = Button(leftFrame, text="START", fg="red", command=start)
    button5 = Button(leftFrame, text="DEBUG", fg="red", command=debugger)
    button2 = Button(leftFrame, text="CheckBox", fg="red", command=checkboxy)
    button4 = Button(leftFrame, text="EXIT", fg="red", command=root.quit)
    button3 = Button(leftFrame, text="PrintScreen", fg="red", command=screen)

    label1.grid(row=0)
    label2.grid(row=1)
    label3.grid(row=2)
    label4.grid(row=3)
    label5.grid(row=4)
    label6.grid(row=5)
    button1.grid(row=1, column=1)
    button2.grid(row=2, column=1)
    button3.grid(row=3, column=1)
    button4.grid(row=4, column=1)
    button5.grid(row=5, column=1)

    Label(rightFrame, textvariable=INFO1, fg="red").pack(side=TOP)
    Label(rightFrame, textvariable=INFO2, fg="red").pack(side=TOP)

    CheckVar = IntVar(value=OTW)
    CheckVar2 = IntVar(value=MULTI)
    CheckVar3 = IntVar(value=ZAPIS)
    CheckVar4 = IntVar(value=USUN)

    check1 = Checkbutton(rightFrame, text="MultiClient", command=mlt, variable=CheckVar2)
    check2 = Checkbutton(rightFrame, text="Otwieranie Rybek", command=otw, variable=CheckVar)
    check3 = Checkbutton(rightFrame, text="ZAPIS PNG", command=zap, variable=CheckVar3)
    check4 = Checkbutton(rightFrame, text="Usuwaj Śmieci", command=usu, variable=CheckVar4)
    check3.pack(side=TOP)
    check1.pack(side=TOP)
    check4.pack(side=TOP)
    check2.pack(side=TOP)

    root.protocol('WM_DELETE_WINDOW', root.quit)
    debuguj()
    root.mainloop()


def checkboxy():
    global INFO1
    global INFO2
    INFO1.set("TEST checkboxow")
    if MULTI == 1:
        INFO2.set("TEST checkboxow")

    koordyLoga1 = szukajloga(1)
    if (koordyLoga1 == 0):
        print("nie znaleziono loga gry")
        INFO1.set("Brak Loga po lewej stronie ekranu")
        return 2  # 2 brak loga

    if (MULTI == 1):
        koordyLoga2 = szukajloga(2)
        if (koordyLoga2 == 0):
            print("nie znaleziono loga gry")
            INFO2.set("Brak Loga po prawej stronie ekranu")
            return 2

    # OKNO1
    oknostart1 = koordyLoga1
    okno1 = oknostart1[0] + 780, oknostart1[1] + 610
    ekipunek1 = szukajwoknie(oknostart1, okno1, sample["eq.png"])

    if (ekipunek1 == 0):
        INFO1.set("nie znaleziono ekwipunku w 1 kliencie")
    else:
        #pozycja wzgledem probki
        oknoeqS1 = ekipunek1[0] + 15, ekipunek1[1] - 70
        #rozmiar
        oknoeq1 = oknoeqS1[0] + 165, oknoeqS1[1] + 295

    chat1 = szukajwoknie(oknostart1,okno1,sample["chat.png"])
    if(chat1 == 0):
        INFO1.set("nie znaleziono CHATU w 1 kliencie")
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
            INFO2.set("nie znaleziono ekwipunku w 2 kliencie")
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
    print("Wielkoryb v1.8")
    main()


