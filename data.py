import sys
from enum import Enum

# Bazowy config
DATA = {
	"Otwieraj_Ryby": 0,
	"Zapis_Screenow": 0,
	"Usuwaj_Smieci": 0,
	"Rozdzielczosc_Klienta": 1,
	"Klient_1": 1,
	"Klient_2": 0,
	"Klient_3": 0,
	"Klient_4": 0
}

MAX_CLIENTS = 4


def read_config():
	configRead = open('config.txt', 'r')
	for line in configRead:
		for data, values in DATA.items():
			if (line.split()[0] == data):
				DATA[data] = line.split()[1]
	configRead.close()


def write_config():
	configWrite = open('config.txt', 'w')
	configWrite.write("Config Bota:\n")
	for data, values in DATA.items():
		configWrite.write(f"{data} {values}\n")
	configWrite.write("** 1=640:360 / 0=800:600 rozdzielczosc klienta")
	configWrite.close()


read_config()
