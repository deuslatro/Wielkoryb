from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from UI_okno import Ui_MainWindow
import data
import wedkarz
import threading
import mouse



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
		self.ui.pushButton1.clicked.connect(self.startBots)
		self.ui.pushButton2.clicked.connect(self.stopBots)
		self.ui.checkRes1.clicked.connect(self.pressCheckRes1)
		self.ui.checkRes2.clicked.connect(self.pressCheckRes2)
		self.ui.checkOpcje1.clicked.connect(self.pressOpcjeCheck1)
		self.ui.checkOpcje2.clicked.connect(self.pressOpcjeCheck2)
		self.ui.buttonOpcje1.clicked.connect(self.pressOpcjeButton1)
		self.ui.checkBot1.clicked.connect(self.pressCheckBot1)
		self.ui.checkBot2.clicked.connect(self.pressCheckBot2)
		self.ui.checkBot3.clicked.connect(self.pressCheckBot3)
		self.ui.checkBot4.clicked.connect(self.pressCheckBot4)
		self.ui.checkDebug1.clicked.connect(self.pressCheckDebug1)
		self.checkBoxStatus()
		self.ui.checkOpcje1.setDisabled(True)
		self.ui.checkOpcje2.setDisabled(True)
		self.ui.checkOpcje3.setDisabled(True)
		self.ui.buttonDebug1.clicked.connect(self.pressDebug1)
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.botsStatus)
		self.timer.start(1000)

	def botsStatus(self):
		self.ui.labelBot7.setText(data.STATUS[0])
		self.ui.labelBot7.update()
		self.ui.labelBot8.setText(data.STATUS[1])
		self.ui.labelBot8.update()
		self.ui.labelBot9.setText(data.STATUS[2])
		self.ui.labelBot9.update()
		self.ui.labelBot10.setText(data.STATUS[3])
		self.ui.labelBot10.update()
		if all(flag == "OFF" for (flag) in data.STATUS):
			self.ui.pushButton1.setDisabled(False)
			self.ui.pushButton2.setDisabled(True)


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

	def pressDebug1(self):
		sample=self.ui.comboDebug.itemText(self.ui.comboDebug.currentIndex())
		if sample == "lowienie":
			wedkarz.probka(wedkarz.sample["low.png"])
		elif sample == "przyneta":
			wedkarz.probka(wedkarz.sample["robak.png"])
		else:
			wedkarz.probka(wedkarz.ryby[f"{sample}.png"])

	def pressCheckBot1(self):
		if self.ui.checkBot1.isChecked():
			data.DATA["Klient_1"] = 1
		else:
			data.DATA["Klient_1"] = 0


	def pressCheckBot2(self):
		if self.ui.checkBot2.isChecked():
			data.DATA["Klient_2"] = 1
		else:
			data.DATA["Klient_2"] = 0

	def pressCheckBot3(self):
		if self.ui.checkBot3.isChecked():
			data.DATA["Klient_3"] = 1
		else:
			data.DATA["Klient_3"] = 0

	def pressCheckBot4(self):
		if self.ui.checkBot4.isChecked():
			data.DATA["Klient_4"] = 1
		else:
			data.DATA["Klient_4"] = 0



	def collectButtonsToList(self):
		return [self.ui.checkBot1, self.ui.checkBot2, self.ui.checkBot3, self.ui.checkBot4]

	def stopBots(self):
		data.THREAD_STOP = 1
		wedkarz.stop()
		self.ui.pushButton1.setDisabled(False)
		self.ui.pushButton2.setDisabled(True)
		self.ui.pushButton_opcje.setDisabled(False)
		self.ui.checkBot1.setDisabled(False)
		self.ui.checkBot2.setDisabled(False)
		self.ui.checkBot3.setDisabled(False)
		self.ui.checkBot4.setDisabled(False)
		self.ui.checkRes1.setDisabled(False)
		self.ui.checkRes2.setDisabled(False)

	#Naciesniecie zmiany rozdzialki
	def pressCheckRes1(self):
		data.DATA["Rozdzielczosc_Klienta"] = 1
		self.ui.checkRes1.setChecked(True)
		self.ui.checkRes2.setChecked(False)


	def pressCheckRes2(self):
		data.DATA["Rozdzielczosc_Klienta"] = 0
		self.ui.checkRes2.setChecked(True)
		self.ui.checkRes1.setChecked(False)


	def pressCheckDebug1(self):
		if self.ui.checkDebug1.isChecked():
			data.DATA["Zapis_Screenow"] = 1
		else:
			data.DATA["Zapis_Screenow"] = 0

	def pressOpcjeCheck1(self):
		if self.ui.checkOpcje1.isChecked():
			data.DATA["Otwieraj_Ryby"] = 1
		else:
			data.DATA["Otwieraj_Ryby"] = 0

	def pressOpcjeButton1(self):
		data.write_config()

	def pressOpcjeCheck2(self):
		if self.ui.checkOpcje2.isChecked():
			data.DATA["Usuwaj_Smieci"] = 1
		else:
			data.DATA["Usuwaj_Smieci"] = 0

	def checkResolution(self):
		if self.ui.checkRes1.isChecked():
			data.DATA["Rozdzielczosc_Klienta"] = 1
		else:
			data.DATA["Rozdzielczosc_Klienta"] = 0

	def coutCheckedBots(self):
		numberOfBots = 0
		buttonList = self.collectButtonsToList()
		for button in buttonList:
			if button.isChecked():
				numberOfBots += 1
		print(numberOfBots)
		return numberOfBots

	def startBots(self):
		for i in range(0,self.coutCheckedBots()):
			data.STATUS[i] = "LOAD"
		self.checkResolution()
		data.THREAD_STOP = 0
		wedkarz.startNewBots(self.coutCheckedBots())
		thread = threading.Thread(target=mouse.queueOperator, name='mouse',daemon=True)
		thread.start()
		self.ui.pushButton1.setDisabled(True)
		self.ui.pushButton2.setDisabled(False)
		self.ui.pushButton_opcje.setDisabled(True)
		self.ui.checkBot1.setDisabled(True)
		self.ui.checkBot2.setDisabled(True)
		self.ui.checkBot3.setDisabled(True)
		self.ui.checkBot4.setDisabled(True)
		self.ui.checkRes1.setDisabled(True)
		self.ui.checkRes2.setDisabled(True)


	def checkBoxStatus(self):
		if data.DATA.get("Rozdzielczosc_Klienta") == '1':
			self.pressCheckRes2()
			self.pressCheckRes1()
		else:
			self.pressCheckRes2()
		if (data.DATA.get("Otwieraj_Ryby")) == '1':
			self.ui.checkOpcje1.setChecked(True)
			self.ui.checkOpcje1.update()
		else:
			self.ui.checkOpcje1.setChecked(False)
		if data.DATA.get("Usuwaj_Smieci") == '1':
			self.ui.checkOpcje2.setChecked(True)
		else:
			self.ui.checkOpcje2.setChecked(False)
		if data.DATA.get("Klient_1") == '1':
			self.ui.checkBot1.setChecked(True)
		if data.DATA.get("Klient_2") == '1':
			self.ui.checkBot2.setChecked(True)
		if data.DATA.get("Klient_3") == '1':
			self.ui.checkBot3.setChecked(True)
		if data.DATA.get("Klient_4") == '1':
			self.ui.checkBot4.setChecked(True)
		if data.DATA.get("Zapis_Screenow") == '1':
			self.ui.checkDebug1.setChecked(True)