import time
import os
import random
import numpy
import pyautogui
import PIL
from tkinter import *
from PIL import ImageGrab, ImageDraw, Image
import cv2

# wczytanie pozostalych grafik
robak = Image.open("img/robak.png")
low = Image.open("img/lowienie.png")
eq = Image.open("img/eq.png")
plaszcz = Image.open("img/plaszcz.png")
pierscien = Image.open("img/pierscien.png")
kosz = Image.open("img/kosz.png")
usuwanie = Image.open("img/usun.png")
puste = Image.open("img/puste.png")

liczby = []
for i in range(1, 7):
    liczbaStr = ("img/liczby/liczba" + str(i) + ".png")
    liczbaTmp = cv2.imread(liczbaStr)
    print(liczbaStr)
    liczby.append(liczbaTmp)

ryby = []
for i in range(1, 13):
    rybaStr = ("img/ryby/ryba" + str(i) + ".png")
    rybaTmp = cv2.imread(rybaStr)
    print(rybaStr)
    ryby.append(rybaTmp)

pyautogui.PAUSE = 0
pyautogui.FAILSAFE = False

pustybit = (0, 15, 255)
bialybit = (255, 255, 255)

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
    logo = Image.open("img/logo.png")
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


def test():
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


def debuguj():
    global DEBUGGER
    global debug
    OPTIONS = [
        "ROBAK",
        "WEDKA",
        "Karas",
        "Mandaryna",
        "Duzy Karas",
        "Karp",
        "Slodka Ryba",
        "Shiri",
        "Plaszcz Uciekiniera",
        "Pierscien Lucy",
        "Puste",
        "Pstrag",
        "Losos",
        "Amur",
        "nowa1",
        "nowa2",
        "nowa3",
        "TEST"
    ]
    variable = StringVar(debug)
    variable.set(OPTIONS[0])
    w = OptionMenu(debug, variable, *OPTIONS)
    w.pack()
    debug.title("DEBUGGER v2.0")
    kolor = "gray"
    leftFrame = Frame(debug, bg=kolor)
    leftFrame.pack(side=LEFT)
    rightFrame = Frame(debug)
    rightFrame.pack(side=LEFT)
    middleFrame = Frame(debug, bg=kolor)
    middleFrame.pack(side=LEFT)
    buttons = Button(debug, text="PODMIEN", fg="red", command=lambda: probka(variable.get()))
    buttons.pack()
    button5 = Button(leftFrame, text="TEST", fg="red", command=test2)
    button5.pack()
    label0 = Label(debug, fg="red", text="DEBUGER słóży do podmieniania podstawowych grafik nawigujących bota")
    label0.pack()
    label1 = Label(debug, fg="red",
                   text="Pobiera i nadpisuje próbke danego przedmiotu z pierwszego slota EQ/ ikonke lowienia z F4")
    label1.pack()
    label2 = Label(debug, fg="red", text="By zamknac debuger uzyj ponownie klawisza DEBUG")
    label2.pack()
    label3 = Label(debug, fg="red", text="DEBUGER nie działa z włączonym MULTICLIENT")
    label3.pack()
    DEBUGGER = 0
    debug.protocol('WM_DELETE_WINDOW', debug.withdraw)
    debug.withdraw()
    debug.mainloop()


def probka(a):
    (oknostart1, okno1, oknoMaleS1, oknoMale1, oknoeqS1, oknoeq1, ekipunek1) = checkboxy()
    boxS = oknoeqS1[0] + 16, oknoeqS1[1] + 14
    boxE = oknoeqS1[0] + 24, oknoeqS1[1] + 20
    global ryby
    global plaszcz
    global pierscien
    global puste
    global robak
    global low
    img = ImageGrab.grab(bbox=boxS + boxE)
    print("pobieram probke:", a)
    if a == "Karas":
        ryby[0] = img
        img.save("img/ryby/ryba1.png")
        print("zmieniono " + a)
    elif a == "Mandaryna":
        ryby[1] = img
        img.save("img/ryby/ryba2.png")
        print("zmieniono " + a)
    elif a == "Duzy Karas":
        ryby[2] = img
        img.save("img/ryby/ryba3.png")
        print("zmieniono " + a)
    elif a == "Karp":
        ryby[3] = img
        img.save("img/ryby/ryba4.png")
        print("zmieniono " + a)
    elif a == "Slodka Ryba":
        ryby[4] = img
        img.save("img/ryby/ryba5.png")
        print("zmieniono " + a)
    elif a == "Plaszcz Uciekiniera":
        plaszcz = img
        img.save("img/plaszcz.png")
        print("zmieniono " + a)
    elif a == "Pierscien Lucy":
        pierscien = img
        img.save("img/pierscien.png")
        print("zmieniono " + a)
    elif a == "ROBAK":
        robak = img
        img.save("img/robak.png")
        print("zmieniono " + a)
    elif a == "Shiri":
        ryby[5] = img
        img.save("img/ryby/ryba12.png")
        print("zmieniono " + a)
    elif a == "nowa3":
        ryby[6] = img
        img.save("img/ryby/ryba6.png")
        print("zmieniono " + a)
    elif a == "Pstrag":
        ryby[7] = img
        img.save("img/ryby/ryba7.png")
        print("zmieniono " + a)
    elif a == "Losos":
        ryby[8] = img
        img.save("img/ryby/ryba8.png")
        print("zmieniono " + a)
    elif a == "Amur":
        ryby[9] = img
        img.save("img/ryby/ryba9.png")
        print("zmieniono " + a)
    elif a == "nowa1":
        ryby[10] = img
        img.save("img/ryby/ryba10.png")
        print("zmieniono " + a)
    elif a == "nowa2":
        ryby[11] = img
        img.save("img/ryby/ryba11.png")
        print("zmieniono " + a)
    elif a == "Puste":
        puste = img
        img.save("img/puste.png")
        print("zmieniono " + a)
    elif a == "WEDKA":
        boxWS = oknostart1[0] + 560, oknostart1[1] + 580
        boxWE = oknostart1[0] + 570, oknostart1[1] + 600
        img = ImageGrab.grab(bbox=boxWS + boxWE)
        low = img
        img.save("img/lowienie.png")
        print("zmieniono " + a)
    elif a == "TEST":
        pierscien = img
        img.save("test.png")
        print("zmieniono " + a)


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

    first = szukajwoknie(oknostart, okno, kosz)
    if first == 0:
        INFO1.set("okno usuwania")
        INFO2.set("jest nieosiagalne")
        Tk.update(root)
        time.sleep(5)
        return 0
    move(first)
    second = szukajwoknie(oknostart, okno, usuwanie)
    if second == 0:
        INFO1.set("przycisk usuwania")
        INFO2.set("jest nieosiągalny")
        Tk.update(root)
        time.sleep(5)
        return 0
    border1 = second[0] - 50, second[1] - 215
    border2 = border1[0] + 170, border1[1] + 200

    for i in range(8):  # 0 - 7
        item1 = szukajwoknie(oknoeq1, oknoeq2, pierscien)
        if (item1 != 0):
            slot = szukajwoknie(border1, border2, puste)
            pyautogui.moveTo(item1[0], item1[1], 0.2)
            time.sleep(0.2)
            pyautogui.dragTo(slot[0], slot[1], 0.3)

        item2 = szukajwoknie(oknoeq1, oknoeq2, plaszcz)
        if (item2 != 0):
            print("plaszcz")
            slot = szukajwoknie(border1, border2, puste)
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
    INFO1.set("STARTOWANIE")
    INFO2.set("NIEAKTYWNY")
    Tk.update(root)
    koordyrobaka1 = szukajwoknie(oknostart1, okno1, robak)
    if (koordyrobaka1 == 0):
        INFO1.set("nie odnaleziono robaka")
        Tk.update(root)
        return 0
    # szukaj lowienia
    koordylowienia1 = szukajwoknie(oknostart1, okno1, low)
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
    (oknostart1, okno1, oknoMaleS1, oknoMale1, oknoeqS1, oknoeq1, ekipunek1, oknostart2, okno2, oknoMaleS2, oknoMale2,
     oknoeqS2, oknoeq2, ekwipunek2) = checkboxy()

    sprawdzanie = 10
    global INFO1
    global INFO2
    global RESTART
    INFO1.set("STARTOWANIE")
    INFO2.set("STARTOWANIE")
    Tk.update(root)

    koordyrobaka1 = szukajwoknie(oknostart1, okno1, robak)
    if (koordyrobaka1 == 0):
        INFO1.set("nie odnaleziono robaka")
        return 0
    koordylowienia1 = szukajwoknie(oknostart1, okno1, low)
    if (koordylowienia1 == 0):
        INFO1.set("nie odnaleziono wedki")
        return 0

    koordyrobaka2 = szukajwoknie(oknostart2, okno2, robak)
    if (koordyrobaka2 == 0):
        INFO2.set("nie odnaleziono robaka")
        return 0
    koordylowienia2 = szukajwoknie(oknostart2, okno2, low)
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
    sample = cv2.imread("img/liczby/okno.png")
    probability = []
    szukane = active_search(sample, image)
    if isinstance(szukane, int):
        # ilosc  prob przed restartem
        if MULTI == 1:
            if (k > 600):
                return 7
        # ustalenie po ilu powtórzeniach restart
        if (k > 900):
            return 7
        return 0
    else:
        print("wyskoczylo okno")
        for i in range(0, 6):
            # print("sprawdzam liczbe o indeksie",i)
            number = liczby[i]
            probability.append(which_number(number, szukane))
            if (probability[i] == 0):
                print("znaleziono", i + 1)
                return (i + 1)
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
        for i in range(0, 12):
            ryba = szukajwoknie(oknoeq1, oknoeq2, ryby[i])
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
    root.title("Wędkarz v.3.5")
    kolor = "gray"
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

    label1 = Label(leftFrame, text="Wędkarz v.3.5", fg="blue", bg=kolor)
    label2 = Label(leftFrame, text="Wystartuj Bota", fg="cyan", bg=kolor)
    label6 = Label(leftFrame, text="DEBUGGER", fg="cyan", bg="red")
    label3 = Label(leftFrame, text="CheckBox", fg="cyan", bg=kolor)
    label5 = Label(leftFrame, text="Wyjscie", fg="cyan", bg=kolor)
    label4 = Label(leftFrame, text="PRINTSCREEN", fg="cyan", bg=kolor)

    button1 = Button(leftFrame, text="START", fg="red", command=start)
    button5 = Button(leftFrame, text="DEBUG", fg="red", command=test)
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

    label6 = Label(middleFrame, text="Jedno okno po lewej ,drugie po prawej stronie.", fg="blue", bg=kolor)
    label6.pack(side=TOP)
    label7 = Label(middleFrame,
                   text="Otwórze eq, na zakładce z robakami / schowaj eq i wyjmij wędkę z wody by ZASTOPOWAC.",
                   fg="blue", bg=kolor)
    label7.pack(side=TOP)
    label8 = Label(middleFrame, text="Nie zasłaniaj okien gry innymi programami!", fg="blue", bg=kolor)
    label8.pack(side=TOP)
    label9 = Label(middleFrame,
                   text="Zaznacz ZAPIS i użyj checkboxa by sprawdzić czy wykrywa ci klienta gry.(tworzy plik PNG)",
                   fg="blue", bg=kolor)
    label9.pack(side=TOP)
    label10 = Label(middleFrame, text="Multiclient oznacza że program obsługuje dokładnie 2 klienty naraz.", fg="blue",
                    bg=kolor)
    label10.pack(side=TOP)
    label11 = Label(middleFrame,
                    text="Otwieranie rybek wyłącz tylko w przypadku krotkiego łowienia by nie przepełnić eq.",
                    fg="blue", bg=kolor)
    label11.pack(side=TOP)

    label11 = Label(rightFrame, text="INFO:", fg="red")
    label11.pack(side=TOP)
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
    oknoMaleS1 = oknostart1[0] + 355, oknostart1[1] + 200
    oknoMale1 = oknoMaleS1[0] + 90, oknoMaleS1[1] + 70
    ekipunek1 = szukajwoknie(oknostart1, okno1, eq)
    if (ekipunek1 == 0):
        INFO1.set("nie znaleziono ekwipunku w 1 kliencie")
    oknoeqS1 = ekipunek1[0] - 10, ekipunek1[1] - 350
    oknoeq1 = oknoeqS1[0] + 165, oknoeqS1[1] + 295

    # OKNO2
    if (MULTI == 1):
        oknostart2 = koordyLoga2
        okno2 = oknostart2[0] + 780, oknostart2[1] + 610
        oknoMaleS2 = oknostart2[0] + 355, oknostart2[1] + 200
        oknoMale2 = oknoMaleS2[0] + 90, oknoMaleS2[1] + 70
        ekipunek2 = szukajwoknie(oknostart2, okno2, eq)
        if (ekipunek2 == 0):
            INFO2.set("nie znaleziono ekwipunku w 2 kliencie")
        oknoeqS2 = ekipunek2[0] - 10, ekipunek2[1] - 350
        oknoeq2 = oknoeqS2[0] + 165, oknoeqS2[1] + 295

    if ZAPIS == 1:
        img = ImageGrab.grab(bbox=None)
        draw = ImageDraw.Draw(img)
        rysujokno1 = oknostart1 + okno1
        rysujoknoM1 = oknoMaleS1 + oknoMale1
        rysujeq1 = oknoeqS1 + oknoeq1
        # rysowanie
        draw.rectangle(rysujokno1, outline=128, width=3)
        draw.rectangle(rysujoknoM1, outline=(32, 0, 255), width=3)
        draw.rectangle(rysujeq1, outline=(64, 255, 128), width=3)

        if (MULTI == 1):
            rysujokno2 = oknostart2 + okno2
            rysujoknoM2 = oknoMaleS2 + oknoMale2
            rysujeq2 = oknoeqS2 + oknoeq2
            # rysowanie
            draw.rectangle(rysujokno2, outline=128, width=3)
            draw.rectangle(rysujoknoM2, outline=(32, 0, 255), width=3)
            draw.rectangle(rysujeq2, outline=(64, 255, 128), width=3)
        img.save("boxy.png")
        time.sleep(0.5)

    if MULTI == 1:
        return (oknostart1, okno1, oknoMaleS1, oknoMale1, oknoeqS1, oknoeq1, ekipunek1, oknostart2, okno2, oknoMaleS2,
                oknoMale2, oknoeqS2, oknoeq2, ekipunek2)
    if MULTI == 0:
        return (oknostart1, okno1, oknoMaleS1, oknoMale1, oknoeqS1, oknoeq1, ekipunek1)


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


print("Wielkoryb v1.6")
main()
