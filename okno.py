from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QDesktopWidget, \
	QGraphicsColorizeEffect
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor, QPixmap,QFont
from PyQt5.QtCore import Qt, QPoint
from UI_okno import Ui_MainWindow
import data
import wedkarz
import threading
import mouse
from random import randint
import disbot



class GameBox(QWidget):
	def __init__(self):
		super().__init__()
		layout = QVBoxLayout()
		myFont = QFont()
		myFont.setBold(True)
		self.label1 = QLabel("OKNO GRY")
		self.label1.setFont(myFont)
		color_effect = QGraphicsColorizeEffect()
		color_effect.setColor(Qt.red)
		self.label1.setGraphicsEffect(color_effect)
		layout.addWidget(self.label1)
		self.setLayout(layout)
		self.qp = QPainter()
		# self.paintEvent()
		# self.location_on_the_screen()

	def location_on_the_screen(self,logoPosition):
		self.hide()
		if logoPosition != 0:
			x = logoPosition[0]
			y = logoPosition[1]
			self.move(x, y)
		self.show()

	def paintEvent(self, event):
		GameWidth = wedkarz.GameSize[0]
		GameHeight = wedkarz.GameSize[1]
		self.qp.begin(self)
		self.qp.setPen(QPen(Qt.red, 4, Qt.SolidLine))
		self.qp.drawRect(0, 0, GameWidth, GameHeight)
		self.qp.end()



class EQBox(QWidget):
	def __init__(self,eqWindow):
		super().__init__()
		layout = QVBoxLayout()
		myFont = QFont()
		myFont.setBold(True)
		self.label1 = QLabel("Probka z EQ")
		self.label1.setFont(myFont)
		color_effect = QGraphicsColorizeEffect()
		color_effect.setColor(Qt.blue)
		self.label1.setGraphicsEffect(color_effect)
		self.label1.style()
		layout.addWidget(self.label1)
		self.setLayout(layout)
		self.qp = QPainter()
		self.eqWindow = eqWindow
		# self.paintEvent()
		# self.location_on_the_screen()

	def location_on_the_screen(self,eqWindow):
		self.hide()
		if eqWindow != 0:
			x = eqWindow[0]
			y = eqWindow[1]
			self.move(x, y)
		self.show()

	def paintEvent(self, event):
		self.qp.begin(self)
		if self.eqWindow != 0:
			self.qp.setPen(QPen(Qt.blue, 1, Qt.SolidLine))
			self.qp.drawRect(wedkarz.SAMPLE_COORDS[0], wedkarz.SAMPLE_COORDS[1],wedkarz.SAMPLE_SIZE[0],wedkarz.SAMPLE_SIZE[1])
			self.qp.drawRect(0, 0, wedkarz.EQ_SIZE[0],wedkarz.EQ_SIZE[1])
		self.qp.end()


class ChatBox(QWidget):
	def __init__(self,chatWindow):
		super().__init__()
		layout = QVBoxLayout()
		myFont = QFont()
		myFont.setBold(True)
		self.label1 = QLabel("Probka Chatu")
		self.label1.setFont(myFont)
		color_effect = QGraphicsColorizeEffect()
		color_effect.setColor(Qt.red)
		self.label1.setGraphicsEffect(color_effect)
		self.label1.style()
		layout.addWidget(self.label1)
		self.setLayout(layout)
		self.qp = QPainter()
		self.chatWindow = chatWindow
		# self.paintEvent()
		# self.location_on_the_screen()

	def location_on_the_screen(self,chatWindow):
		self.hide()
		if chatWindow != 0:
			x = chatWindow[0]
			y = chatWindow[1]-15
			self.move(x, y)
		self.show()

	def paintEvent(self, event):
		self.qp.begin(self)
		if self.chatWindow!= 0:
			chatLine = 0
			self.qp.setPen(QPen(Qt.red, 1, Qt.SolidLine))
			# self.qp.drawRect(wedkarz.CHAT_COORDS[0], wedkarz.CHAT_COORDS[1],wedkarz.CHAT_SIZE[0],wedkarz.CHAT_SIZE[1])
			for line in range(0, wedkarz.NUMBER_OF_SCANNED_LINE):
				self.qp.drawRect(0, chatLine, wedkarz.CHAT_SIZE[0],wedkarz.CHAT_SIZE[1])
				chatLine += 15
		self.qp.end()

class CloudBox(QWidget):
	def __init__(self,cloudWindow):
		super().__init__()
		layout = QVBoxLayout()
		myFont = QFont()
		myFont.setBold(True)
		self.label1 = QLabel("Poszukiwanie chmurki")
		self.label1.setFont(myFont)
		color_effect = QGraphicsColorizeEffect()
		color_effect.setColor(Qt.cyan)
		self.label1.setGraphicsEffect(color_effect)
		self.label1.style()
		layout.addWidget(self.label1)
		self.setLayout(layout)
		self.qp = QPainter()
		self.cloudWindow = cloudWindow
		# self.paintEvent()
		# self.location_on_the_screen()

	def location_on_the_screen(self,cloudWindow):
		self.hide()
		if cloudWindow != 0:
			x = cloudWindow[0]
			y = cloudWindow[1]
			self.move(x, y)
		self.show()

	def paintEvent(self, event):
		self.qp.begin(self)
		if self.cloudWindow!= 0:
			self.qp.setPen(QPen(Qt.cyan, 3, Qt.SolidLine))
			self.qp.drawRect(0, 0, wedkarz.CLOUD_SIZE[0],wedkarz.CLOUD_SIZE[1])
		self.qp.end()



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
		self.ui.buttonDebug3.clicked.connect(self.debug_overlay)
		#czy utworzono juz okna
		self.existEQW=0
		self.existGameW=0
		self.existChatW=0





	def debug_overlay(self):
		if (self.existGameW == 1):
			self.gamebox.hide()
			self.cloudbox.hide()
			if(self.existEQW == 1):
				self.eqbox.hide()
			if (self.existChatW == 1):
				self.chatbox.hide()
			if (self.existChatW == 1):
				self.chatbox.hide()
		(logoPosition, gameWindow, chatWindow, msgBox, eqWindow, cloudWindow) = wedkarz.checkBox(1)
		if logoPosition == 0:
			print("Logo ERR")
		else:
			self.gamebox = GameBox()
			self.existGameW=1
			self.gamebox.setFixedSize(860, 660)
			self.gamebox.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
			self.gamebox.setAttribute(QtCore.Qt.WA_TranslucentBackground, on=True)

			self.eqbox = EQBox(eqWindow)
			self.existEQW=1
			self.eqbox.setFixedSize(200, 400)
			self.eqbox.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
			self.eqbox.setAttribute(QtCore.Qt.WA_TranslucentBackground, on=True)

			self.chatbox = ChatBox(chatWindow)
			self.existChatW=1
			self.chatbox.setFixedSize(100, 100)
			self.chatbox.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
			self.chatbox.setAttribute(QtCore.Qt.WA_TranslucentBackground, on=True)

			self.cloudbox = CloudBox(cloudWindow)
			# uzalezione od pozycji loga
			self.cloudbox.setFixedSize(170, 70)
			self.cloudbox.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
			self.cloudbox.setAttribute(QtCore.Qt.WA_TranslucentBackground, on=True)


			self.eqbox.location_on_the_screen(eqWindow)
			self.chatbox.location_on_the_screen(chatWindow)
			self.cloudbox.location_on_the_screen(cloudWindow)
			self.gamebox.location_on_the_screen(logoPosition)




		# self.w.location_on_the_screen(self.w)
		# self.w.paintEvent(self.w)
		# self.paintEvent(1)


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
		sample = self.ui.comboDebug.itemText(self.ui.comboDebug.currentIndex())
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

	# Naciesniecie zmiany rozdzialki
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
		for i in range(0, self.coutCheckedBots()):
			data.STATUS[i] = "LOAD"
		self.checkResolution()
		data.THREAD_STOP = 0
		wedkarz.startNewBots(self.coutCheckedBots())
		thread = threading.Thread(target=mouse.queueOperator, name='mouse', daemon=True)
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
