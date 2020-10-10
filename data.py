import os
from PIL import  Image
import numpy as np

# Bazowy config
DATA = {
	"Otwieraj_Ryby": 0,
	"Zapis_Screenow": 0,
	"Discord_Bot": 1,
	"Rozdzielczosc_Klienta": 1,
	"Klient_1": 1,
	"Klient_2": 0,
	"Klient_3": 0,
	"Klient_4": 0,
	"Fish_Delay": 50,
	"Space_Delay": 50,
	"until_Restart": 350
}


MAX_CLIENTS = 4

#aktualizuje okno bota do zamkniecia watkow


MOUSE = 1
STATUS = []
STATUS.append("OFF")
STATUS.append("OFF")
STATUS.append("OFF")
STATUS.append("OFF")


def read_config():
	configRead = open('config.txt', 'r')
	for line in configRead:
		for data, values in DATA.items():
			if (line.split()[0] == data):
				DATA[data] = line.split()[1]
	configRead.close()

read_config()


def write_config():
	configWrite = open('config.txt', 'w')
	configWrite.write("Config Bota:\n")
	for data, values in DATA.items():
		configWrite.write(f"{data} {values}\n")
	configWrite.write("* 1=640:360 / 0=800:600 rozdzielczosc klienta\n")
	configWrite.write("** Delay w ms[1/1000 s] mozna zmniejszac byleby klient metina zdazyl regowac na klikniecia")
	configWrite.write("** until_Restart liczy liczbe iteracji przed restartem (jezeli bot sie restartuje nim wyskoczy lowienie nalezy zwiekszyc)")
	configWrite.close()




# Wczytaj zdjęcia by operować nimi biblioteką PIL(funkcja szukajwoknie)
def load_images_toPIL(folder):
    images = {}
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder, filename))
        if img is not None:
            #print(filename)
            images[filename] = img
    return images

def load_images_toNUMPY(folder):
    images = {}
    for filename in os.listdir(folder):
        data = np.load(os.path.join(folder, filename))
        if data is not None:
            images[filename] = data
    return images
