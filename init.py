import sys
import disbot
#from disbot import signal
from time import sleep
import asyncio

#PRZEKAZYWANIE z kodu do DICORDBOTA
#future = asyncio.run_coroutine_threadsafe(disbot.client.signal("essa"), loop)
#result = future.result()

from PyQt5.QtWidgets import QApplication

from okno import MainWindow

if __name__ == "__main__":
	app = QApplication(sys.argv)
	main_win = MainWindow()
	main_win.show()
	sys.exit(app.exec_())