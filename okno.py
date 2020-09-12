import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from UI_okno import Ui_MainWindow

class MainWindow:
	def __init__(self):
		self.main_win = QMainWindow()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self.main_win)

		self.ui.stackedWidget.setCurrentWidget(self.ui.bot)

		self.ui.pushButton_bot.clicked.connect(self.goBot)
		self.ui.pushButton_opcje.clicked.connect(self.goOpcje)
		self.ui.pushButton_pomoc.clicked.connect(self.goPomoc)
		self.ui.pushButton_log.clicked.connect(self.goLog)
		self.ui.buttonOpcje3.clicked.connect(self.goDebbug)
		self.ui.buttonDebug2.clicked.connect(self.goOpcje)

	def show(self):
		self.main_win.show()

	def goBot(self):
		self.ui.stackedWidget.setCurrentWidget(self.ui.bot)
	def goOpcje(self):
		self.ui.stackedWidget.setCurrentWidget(self.ui.opcje)
	def goPomoc(self):
		self.ui.stackedWidget.setCurrentWidget(self.ui.pomoc)
	def goLog(self):
		self.ui.stackedWidget.setCurrentWidget(self.ui.log)
	def goDebbug(self):
		self.ui.stackedWidget.setCurrentWidget(self.ui.debug)



if __name__ == "__main__":
	app = QApplication(sys.argv)
	main_win = MainWindow()
	main_win.show()
	sys.exit(app.exec_())