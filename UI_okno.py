# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oknofinal.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 265)
        MainWindow.setMinimumSize(QtCore.QSize(320, 265))
        MainWindow.setMaximumSize(QtCore.QSize(320, 265))
        MainWindow.setStyleSheet("background-color=white")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 30, 321, 251))
        self.stackedWidget.setAutoFillBackground(True)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.bot = QtWidgets.QWidget()
        self.bot.setObjectName("bot")
        self.labelBot7 = QtWidgets.QLabel(self.bot)
        self.labelBot7.setGeometry(QtCore.QRect(250, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.labelBot7.setFont(font)
        self.labelBot7.setObjectName("labelBot7")
        self.labelBot4 = QtWidgets.QLabel(self.bot)
        self.labelBot4.setGeometry(QtCore.QRect(190, 70, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelBot4.setFont(font)
        self.labelBot4.setObjectName("labelBot4")
        self.obrazek1 = QtWidgets.QLabel(self.bot)
        self.obrazek1.setGeometry(QtCore.QRect(60, 90, 91, 91))
        self.obrazek1.setText("")
        self.obrazek1.setPixmap(QtGui.QPixmap("img/UI/fishman.png"))
        self.obrazek1.setScaledContents(True)
        self.obrazek1.setObjectName("obrazek1")
        self.labelBot5 = QtWidgets.QLabel(self.bot)
        self.labelBot5.setGeometry(QtCore.QRect(190, 90, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelBot5.setFont(font)
        self.labelBot5.setObjectName("labelBot5")
        self.labelBot9 = QtWidgets.QLabel(self.bot)
        self.labelBot9.setGeometry(QtCore.QRect(250, 90, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.labelBot9.setFont(font)
        self.labelBot9.setObjectName("labelBot9")
        self.checkBot1 = QtWidgets.QCheckBox(self.bot)
        self.checkBot1.setGeometry(QtCore.QRect(170, 50, 16, 17))
        self.checkBot1.setText("")
        self.checkBot1.setChecked(True)
        self.checkBot1.setAutoRepeat(False)
        self.checkBot1.setAutoExclusive(False)
        self.checkBot1.setObjectName("checkBot1")
        self.obrazek2 = QtWidgets.QLabel(self.bot)
        self.obrazek2.setEnabled(True)
        self.obrazek2.setGeometry(QtCore.QRect(0, 0, 321, 241))
        self.obrazek2.setAutoFillBackground(True)
        self.obrazek2.setText("")
        self.obrazek2.setPixmap(QtGui.QPixmap("img/UI/lake.png"))
        self.obrazek2.setScaledContents(True)
        self.obrazek2.setObjectName("obrazek2")
        self.checkBot2 = QtWidgets.QCheckBox(self.bot)
        self.checkBot2.setGeometry(QtCore.QRect(170, 70, 16, 17))
        self.checkBot2.setText("")
        self.checkBot2.setObjectName("checkBot2")

        self.labelBot2 = QtWidgets.QLabel(self.bot)
        self.labelBot2.setGeometry(QtCore.QRect(-20, 0, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.labelBot2.setFont(font)
        self.labelBot2.setLineWidth(1)
        self.labelBot2.setTextFormat(QtCore.Qt.AutoText)
        self.labelBot2.setScaledContents(False)
        self.labelBot2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBot2.setObjectName("labelBot2")
        self.checkBot4 = QtWidgets.QCheckBox(self.bot)
        self.checkBot4.setGeometry(QtCore.QRect(170, 110, 16, 17))
        self.checkBot4.setText("")
        self.checkBot4.setText("")
        self.checkBot4.setObjectName("checkBot4")
        self.labelBot3 = QtWidgets.QLabel(self.bot)
        self.labelBot3.setGeometry(QtCore.QRect(190, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelBot3.setFont(font)
        self.labelBot3.setObjectName("labelBot3")
        self.pushButton1 = QtWidgets.QPushButton(self.bot)
        self.pushButton1.setGeometry(QtCore.QRect(0, 180, 121, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        self.labelBot8 = QtWidgets.QLabel(self.bot)
        self.labelBot8.setGeometry(QtCore.QRect(250, 70, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.labelBot8.setFont(font)
        self.labelBot8.setObjectName("labelBot8")
        self.labelBot10 = QtWidgets.QLabel(self.bot)
        self.labelBot10.setGeometry(QtCore.QRect(250, 110, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.labelBot10.setFont(font)
        self.labelBot10.setObjectName("labelBot10")
        self.labelBot1 = QtWidgets.QLabel(self.bot)
        self.labelBot1.setGeometry(QtCore.QRect(190, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelBot1.setFont(font)
        self.labelBot1.setObjectName("labelBot1")
        self.checkBot3 = QtWidgets.QCheckBox(self.bot)
        self.checkBot3.setGeometry(QtCore.QRect(170, 90, 16, 17))
        self.checkBot3.setText("")
        self.checkBot3.setObjectName("checkBot3")
        self.pushButton2 = QtWidgets.QPushButton(self.bot)
        self.pushButton2.setEnabled(True)
        self.pushButton2.setGeometry(QtCore.QRect(200, 180, 121, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton2.setFont(font)
        self.pushButton2.setObjectName("pushButton2")
        self.labelBot6 = QtWidgets.QLabel(self.bot)
        self.labelBot6.setGeometry(QtCore.QRect(190, 110, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelBot6.setFont(font)
        self.labelBot6.setObjectName("labelBot6")
        self.checkRes2 = QtWidgets.QCheckBox(self.bot)
        self.checkRes2.setGeometry(QtCore.QRect(90, 70, 70, 17))
        self.checkRes2.setChecked(True)
        self.checkRes2.setObjectName("checkRes2")
        self.checkRes1 = QtWidgets.QCheckBox(self.bot)
        self.checkRes1.setGeometry(QtCore.QRect(90, 90, 70, 17))
        self.checkRes1.setObjectName("checkRes1")
        self.labelBot11 = QtWidgets.QLabel(self.bot)
        self.labelBot11.setGeometry(QtCore.QRect(90, 32, 71, 41))
        self.labelBot11.setWordWrap(True)
        self.labelBot11.setObjectName("labelBot11")
        self.obrazek2.raise_()
        self.labelBot7.raise_()
        self.labelBot4.raise_()
        self.labelBot5.raise_()
        self.labelBot9.raise_()
        self.checkBot1.raise_()
        self.checkBot2.raise_()
        self.labelBot2.raise_()
        self.checkBot4.raise_()
        self.labelBot3.raise_()
        self.pushButton1.raise_()
        self.labelBot8.raise_()
        self.labelBot10.raise_()
        self.labelBot1.raise_()
        self.checkBot3.raise_()
        self.pushButton2.raise_()
        self.labelBot6.raise_()
        self.obrazek1.raise_()
        self.checkRes2.raise_()
        self.checkRes1.raise_()
        self.labelBot11.raise_()
        self.stackedWidget.addWidget(self.bot)
        self.opcje = QtWidgets.QWidget()
        self.opcje.setObjectName("opcje")
        self.picOpcje1 = QtWidgets.QLabel(self.opcje)
        self.picOpcje1.setGeometry(QtCore.QRect(-20, 10, 341, 241))
        self.picOpcje1.setText("")
        self.picOpcje1.setPixmap(QtGui.QPixmap("img/UI/settings.png"))
        self.picOpcje1.setScaledContents(True)
        self.picOpcje1.setObjectName("picOpcje1")
        self.buttonOpcje2 = QtWidgets.QPushButton(self.opcje)
        self.buttonOpcje2.setGeometry(QtCore.QRect(10, 180, 181, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonOpcje2.setFont(font)
        self.buttonOpcje2.setObjectName("buttonOpcje2")
        self.checkOpcje3 = QtWidgets.QCheckBox(self.opcje)
        self.checkOpcje3.setGeometry(QtCore.QRect(10, 90, 171, 21))
        self.checkOpcje3.setChecked(False)
        self.checkOpcje3.setObjectName("checkOpcje3")
        self.checkOpcje1 = QtWidgets.QCheckBox(self.opcje)
        self.checkOpcje1.setGeometry(QtCore.QRect(10, 50, 141, 21))
        self.checkOpcje1.setObjectName("checkOpcje1")
        self.picOpcje2 = QtWidgets.QLabel(self.opcje)
        self.picOpcje2.setGeometry(QtCore.QRect(-20, -30, 351, 181))
        self.picOpcje2.setText("")
        self.picOpcje2.setPixmap(QtGui.QPixmap("img/UI/puste.png"))
        self.picOpcje2.setScaledContents(True)
        self.picOpcje2.setObjectName("picOpcje2")
        self.checkOpcje2 = QtWidgets.QCheckBox(self.opcje)
        self.checkOpcje2.setGeometry(QtCore.QRect(10, 70, 141, 21))
        self.checkOpcje2.setObjectName("checkOpcje2")
        self.buttonOpcje1 = QtWidgets.QPushButton(self.opcje)
        self.buttonOpcje1.setGeometry(QtCore.QRect(10, 130, 121, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonOpcje1.setFont(font)
        self.buttonOpcje1.setObjectName("buttonOpcje1")
        self.labelOpcje1 = QtWidgets.QLabel(self.opcje)
        self.labelOpcje1.setGeometry(QtCore.QRect(-50, 10, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.labelOpcje1.setFont(font)
        self.labelOpcje1.setLineWidth(1)
        self.labelOpcje1.setTextFormat(QtCore.Qt.AutoText)
        self.labelOpcje1.setScaledContents(False)
        self.labelOpcje1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOpcje1.setObjectName("labelOpcje1")
        self.picOpcje3 = QtWidgets.QLabel(self.opcje)
        self.picOpcje3.setGeometry(QtCore.QRect(210, 10, 91, 101))
        self.picOpcje3.setText("")
        self.picOpcje3.setPixmap(QtGui.QPixmap("img/UI/tool.png"))
        self.picOpcje3.setScaledContents(True)
        self.picOpcje3.setObjectName("picOpcje3")
        self.buttonOpcje3 = QtWidgets.QPushButton(self.opcje)
        self.buttonOpcje3.setGeometry(QtCore.QRect(210, 180, 101, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonOpcje3.setFont(font)
        self.buttonOpcje3.setObjectName("buttonOpcje3")
        self.picOpcje2.raise_()
        self.picOpcje1.raise_()
        self.buttonOpcje2.raise_()
        self.checkOpcje3.raise_()
        self.checkOpcje1.raise_()
        self.checkOpcje2.raise_()
        self.buttonOpcje1.raise_()
        self.labelOpcje1.raise_()
        self.picOpcje3.raise_()
        self.buttonOpcje3.raise_()
        self.stackedWidget.addWidget(self.opcje)
        self.pomoc = QtWidgets.QWidget()
        self.pomoc.setObjectName("pomoc")
        self.labelPomoc5 = QtWidgets.QLabel(self.pomoc)
        self.labelPomoc5.setGeometry(QtCore.QRect(10, 110, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelPomoc5.setFont(font)
        self.labelPomoc5.setObjectName("labelPomoc5")
        self.labelPomoc8 = QtWidgets.QLabel(self.pomoc)
        self.labelPomoc8.setGeometry(QtCore.QRect(10, 170, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.labelPomoc8.setFont(font)
        self.labelPomoc8.setObjectName("labelPomoc8")
        self.labalPomoc9 = QtWidgets.QLabel(self.pomoc)
        self.labalPomoc9.setGeometry(QtCore.QRect(10, 90, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labalPomoc9.setFont(font)
        self.labalPomoc9.setObjectName("labalPomoc9")
        self.labelPomoc1 = QtWidgets.QLabel(self.pomoc)
        self.labelPomoc1.setGeometry(QtCore.QRect(10, 210, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.labelPomoc1.setFont(font)
        self.labelPomoc1.setObjectName("labelPomoc1")
        self.labelPomoc2 = QtWidgets.QLabel(self.pomoc)
        self.labelPomoc2.setGeometry(QtCore.QRect(-50, 0, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.labelPomoc2.setFont(font)
        self.labelPomoc2.setLineWidth(1)
        self.labelPomoc2.setTextFormat(QtCore.Qt.AutoText)
        self.labelPomoc2.setScaledContents(False)
        self.labelPomoc2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPomoc2.setObjectName("labelPomoc2")
        self.labelPomoc10 = QtWidgets.QLabel(self.pomoc)
        self.labelPomoc10.setGeometry(QtCore.QRect(20, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelPomoc10.setFont(font)
        self.labelPomoc10.setObjectName("labelPomoc10")
        self.labelPomoc6 = QtWidgets.QLabel(self.pomoc)
        self.labelPomoc6.setGeometry(QtCore.QRect(10, 70, 251, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelPomoc6.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.labelPomoc6.setFont(font)
        self.labelPomoc6.setObjectName("labelPomoc6")
        self.labelPomoc3 = QtWidgets.QLabel(self.pomoc)
        self.labelPomoc3.setGeometry(QtCore.QRect(220, 10, 111, 111))
        self.labelPomoc3.setText("")
        self.labelPomoc3.setPixmap(QtGui.QPixmap("img/UI/question.png"))
        self.labelPomoc3.setScaledContents(True)
        self.labelPomoc3.setObjectName("labelPomoc3")
        self.picPomoc1 = QtWidgets.QLabel(self.pomoc)
        self.picPomoc1.setGeometry(QtCore.QRect(-10, 0, 341, 241))
        self.picPomoc1.setText("")
        self.picPomoc1.setPixmap(QtGui.QPixmap("img/UI/paper.jpg"))
        self.picPomoc1.setScaledContents(True)
        self.picPomoc1.setObjectName("picPomoc1")
        self.labelPomoc4 = QtWidgets.QLabel(self.pomoc)
        self.labelPomoc4.setGeometry(QtCore.QRect(10, 130, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelPomoc4.setFont(font)
        self.labelPomoc4.setObjectName("labelPomoc4")
        self.labelPomoc7 = QtWidgets.QLabel(self.pomoc)
        self.labelPomoc7.setGeometry(QtCore.QRect(10, 150, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.labelPomoc7.setFont(font)
        self.labelPomoc7.setObjectName("labelPomoc7")
        self.labelPomoc11 = QtWidgets.QLabel(self.pomoc)
        self.labelPomoc11.setGeometry(QtCore.QRect(10, 190, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.labelPomoc11.setFont(font)
        self.labelPomoc11.setObjectName("labelPomoc11")
        self.picPomoc1.raise_()
        self.labelPomoc5.raise_()
        self.labelPomoc8.raise_()
        self.labalPomoc9.raise_()
        self.labelPomoc1.raise_()
        self.labelPomoc2.raise_()
        self.labelPomoc10.raise_()
        self.labelPomoc6.raise_()
        self.labelPomoc3.raise_()
        self.labelPomoc4.raise_()
        self.labelPomoc7.raise_()
        self.labelPomoc11.raise_()
        self.stackedWidget.addWidget(self.pomoc)
        self.log = QtWidgets.QWidget()
        self.log.setObjectName("log")
        self.pic1_5 = QtWidgets.QLabel(self.log)
        self.pic1_5.setGeometry(QtCore.QRect(-10, 0, 341, 241))
        self.pic1_5.setText("")
        self.pic1_5.setPixmap(QtGui.QPixmap("img/UI/paper.jpg"))
        self.pic1_5.setScaledContents(True)
        self.pic1_5.setObjectName("pic1_5")
        self.label_24 = QtWidgets.QLabel(self.log)
        self.label_24.setGeometry(QtCore.QRect(-60, 0, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_24.setFont(font)
        self.label_24.setLineWidth(1)
        self.label_24.setTextFormat(QtCore.Qt.AutoText)
        self.label_24.setScaledContents(False)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_32 = QtWidgets.QLabel(self.log)
        self.label_32.setGeometry(QtCore.QRect(220, 10, 91, 81))
        self.label_32.setText("")
        self.label_32.setPixmap(QtGui.QPixmap("img/UI/danger.png"))
        self.label_32.setScaledContents(True)
        self.label_32.setObjectName("label_32")
        self.label_31 = QtWidgets.QLabel(self.log)
        self.label_31.setGeometry(QtCore.QRect(10, 40, 211, 161))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.stackedWidget.addWidget(self.log)
        self.debug = QtWidgets.QWidget()
        self.debug.setObjectName("debug")
        self.buttonDebug3 = QtWidgets.QPushButton(self.debug)
        self.buttonDebug3.setGeometry(QtCore.QRect(10, 180, 181, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonDebug3.setFont(font)
        self.buttonDebug3.setObjectName("buttonDebug3")
        self.comboDebug = QtWidgets.QComboBox(self.debug)
        self.comboDebug.setGeometry(QtCore.QRect(10, 60, 85, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkDebug1 = QtWidgets.QCheckBox(self.debug)
        self.checkDebug1.setGeometry(QtCore.QRect(10, 90, 120, 17))
        self.checkDebug1.setText("Zapis_Checkboxów")
        self.checkDebug1.setObjectName("checkDebug1")
        self.comboDebug.setFont(font)
        self.comboDebug.setAccessibleDescription("")
        self.comboDebug.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboDebug.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboDebug.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboDebug.setObjectName("comboDebug")
        self.comboDebug.addItem("")
        self.comboDebug.addItem("")
        self.comboDebug.addItem("")
        self.comboDebug.addItem("")
        self.comboDebug.addItem("")
        self.comboDebug.addItem("")
        self.comboDebug.addItem("")
        self.comboDebug.addItem("")
        self.comboDebug.addItem("")
        self.comboDebug.addItem("")
        self.comboDebug.addItem("")
        self.comboDebug.addItem("")
        #self.comboDebug.addItem("")
        #self.comboDebug.addItem("")
        #self.comboDebug.addItem("")
        #self.comboDebug.addItem("")
        #self.comboDebug.addItem("")
        self.labelDebug2 = QtWidgets.QLabel(self.debug)
        self.labelDebug2.setGeometry(QtCore.QRect(210, 10, 91, 101))
        self.labelDebug2.setText("")
        self.labelDebug2.setPixmap(QtGui.QPixmap("img/UI/tool.png"))
        self.labelDebug2.setScaledContents(True)
        self.labelDebug2.setObjectName("labelDebug2")
        self.labelDebug3 = QtWidgets.QLabel(self.debug)
        self.labelDebug3.setGeometry(QtCore.QRect(0, -60, 351, 181))
        self.labelDebug3.setText("")
        self.labelDebug3.setPixmap(QtGui.QPixmap("img/UI/puste.png"))
        self.labelDebug3.setScaledContents(True)
        self.labelDebug3.setObjectName("labelDebug3")
        self.labelDebug1 = QtWidgets.QLabel(self.debug)
        self.labelDebug1.setGeometry(QtCore.QRect(-30, 10, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.labelDebug1.setFont(font)
        self.labelDebug1.setLineWidth(1)
        self.labelDebug1.setTextFormat(QtCore.Qt.AutoText)
        self.labelDebug1.setScaledContents(False)
        self.labelDebug1.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDebug1.setObjectName("labelDebug1")
        self.buttonDebug2 = QtWidgets.QPushButton(self.debug)
        self.buttonDebug2.setGeometry(QtCore.QRect(210, 180, 101, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonDebug2.setFont(font)
        self.buttonDebug2.setObjectName("buttonDebug2")
        self.buttonDebug1 = QtWidgets.QPushButton(self.debug)
        self.buttonDebug1.setGeometry(QtCore.QRect(10, 130, 121, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonDebug1.setFont(font)
        self.buttonDebug1.setObjectName("buttonDebug1")
        self.picDebug1 = QtWidgets.QLabel(self.debug)
        self.picDebug1.setGeometry(QtCore.QRect(-20, 10, 341, 241))
        self.picDebug1.setText("")
        self.picDebug1.setPixmap(QtGui.QPixmap("img/UI/settings.png"))
        self.picDebug1.setScaledContents(True)
        self.picDebug1.setObjectName("picDebug1")
        self.labelDebug3.raise_()
        self.picDebug1.raise_()
        self.buttonDebug3.raise_()
        self.comboDebug.raise_()
        self.checkDebug1.raise_()
        self.labelDebug2.raise_()
        self.labelDebug1.raise_()
        self.buttonDebug2.raise_()
        self.buttonDebug1.raise_()
        self.stackedWidget.addWidget(self.debug)
        self.pushButton_pomoc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pomoc.setGeometry(QtCore.QRect(160, -10, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_pomoc.setFont(font)
        self.pushButton_pomoc.setObjectName("pushButton_pomoc")
        self.pushButton_log = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_log.setGeometry(QtCore.QRect(240, -10, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_log.setFont(font)
        self.pushButton_log.setObjectName("pushButton_log")
        self.pushButton_log.setDisabled(True)
        self.pushButton_opcje = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_opcje.setGeometry(QtCore.QRect(80, -10, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_opcje.setFont(font)
        self.pushButton_opcje.setObjectName("pushButton_opcje")
        self.pushButton_bot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_bot.setGeometry(QtCore.QRect(0, -10, 81, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_bot.setFont(font)
        self.pushButton_bot.setObjectName("pushButton_bot")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton1.setDisabled(False)
        self.pushButton2.setDisabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelBot7.setText(_translate("MainWindow", "OFF"))
        self.labelBot4.setText(_translate("MainWindow", "Klient 2:"))
        self.labelBot5.setText(_translate("MainWindow", "Klient 3:"))
        self.labelBot9.setText(_translate("MainWindow", "OFF"))
        self.labelBot2.setText(_translate("MainWindow", "WĘDKARZ v3.3"))
        self.labelBot3.setText(_translate("MainWindow", "Klient 1:"))
        self.pushButton1.setText(_translate("MainWindow", "START (F5)"))
        self.pushButton1.setShortcut(_translate("MainWindow", "F5"))
        self.labelBot8.setText(_translate("MainWindow", "OFF"))
        self.labelBot10.setText(_translate("MainWindow", "OFF"))
        self.labelBot1.setText(_translate("MainWindow", "STATUS:"))
        self.pushButton2.setText(_translate("MainWindow", "STOP (F6)"))
        self.pushButton2.setShortcut(_translate("MainWindow", "F6"))
        self.labelBot6.setText(_translate("MainWindow", "Klient 4:"))
        self.checkRes2.setText(_translate("MainWindow", "800x600"))
        self.checkRes1.setText(_translate("MainWindow", "640x360"))
        self.checkDebug1.setText(_translate("MainWindow", "Zapis_Checkboxów"))
        self.labelBot11.setText(_translate("MainWindow", "Wybierz rozdzielczosc:"))
        self.buttonOpcje2.setText(_translate("MainWindow", "USTAWIENIA FABRYCZNE"))
        self.checkOpcje3.setText(_translate("MainWindow", "Tryb Turbo (przy 4 oknach)"))
        self.checkOpcje1.setText(_translate("MainWindow", "Otwieranie Rybek"))
        self.checkOpcje2.setText(_translate("MainWindow", "Wyrzucanie śmieci"))
        self.buttonOpcje1.setText(_translate("MainWindow", "ZAPISZ OPCJE"))
        self.labelOpcje1.setText(_translate("MainWindow", "OPCJE:"))
        self.buttonOpcje3.setText(_translate("MainWindow", "DEBUGGER"))
        self.labelPomoc5.setText(_translate("MainWindow", "Widoczne w kliencie gry : eq, lowienie"))
        self.labelPomoc8.setText(_translate("MainWindow", "jakiegos z wyzej wymienionych elementów"))
        self.labalPomoc9.setText(_translate("MainWindow", "Okno gry zawsze na wierzchu"))
        self.labelPomoc1.setText(_translate("MainWindow", "Wiecej info w Instrukcja_obslugi.txt"))
        self.labelPomoc2.setText(_translate("MainWindow", "POMOC"))
        self.labelPomoc10.setText(_translate("MainWindow", "TIPY:"))
        self.labelPomoc6.setText(_translate("MainWindow", "Uruchom jako administrator!"))
        self.labelPomoc4.setText(_translate("MainWindow", "ikona (lewy gorny rog okna) oraz OKNO chatu"))
        self.labelPomoc7.setText(_translate("MainWindow", "Err(nazwa) - onacza ze bot nie wykrył"))
        self.labelPomoc11.setText(_translate("MainWindow", "Err(robak) - oznacza brak przynety (restart 10 s)"))
        self.label_24.setText(_translate("MainWindow", "LOG:"))
        self.label_31.setText(_translate("MainWindow", "log"))
        self.buttonDebug3.setText(_translate("MainWindow", "USTAWIENIA FABRYCZNE"))
        self.comboDebug.setItemText(0, _translate("MainWindow", "przyneta"))
        self.comboDebug.setItemText(1, _translate("MainWindow", "lowienie"))
        self.comboDebug.setItemText(2, _translate("MainWindow", "ryba1"))
        self.comboDebug.setItemText(3, _translate("MainWindow", "ryba2"))
        self.comboDebug.setItemText(4, _translate("MainWindow", "ryba3"))
        self.comboDebug.setItemText(5, _translate("MainWindow", "ryba4"))
        self.comboDebug.setItemText(6, _translate("MainWindow", "ryba5"))
        self.comboDebug.setItemText(7, _translate("MainWindow", "ryba6"))
        self.comboDebug.setItemText(8, _translate("MainWindow", "ryba7"))
        self.comboDebug.setItemText(9, _translate("MainWindow", "ryba8"))
        self.comboDebug.setItemText(10, _translate("MainWindow", "ryba9"))
        self.comboDebug.setItemText(11, _translate("MainWindow", "ryba10"))
        #self.comboDebug.setItemText(12, _translate("MainWindow", "smiec1"))
        #self.comboDebug.setItemText(13, _translate("MainWindow", "smiec2"))
        #self.comboDebug.setItemText(14, _translate("MainWindow", "smiec3"))
        #self.comboDebug.setItemText(15, _translate("MainWindow", "smiec4"))
        #self.comboDebug.setItemText(16, _translate("MainWindow", "smiec5"))
        self.labelDebug1.setText(_translate("MainWindow", "DEBUGGER:"))
        self.buttonDebug2.setText(_translate("MainWindow", "OPCJE"))
        self.buttonDebug1.setText(_translate("MainWindow", "PODMIEŃ"))
        self.pushButton_pomoc.setText(_translate("MainWindow", "POMOC(F3)"))
        self.pushButton_pomoc.setShortcut(_translate("MainWindow", "F3"))
        self.pushButton_log.setText(_translate("MainWindow", "LOG(F4)"))
        self.pushButton_log.setShortcut(_translate("MainWindow", "F4"))
        self.pushButton_opcje.setText(_translate("MainWindow", "OPCJE(F2)"))
        self.pushButton_opcje.setShortcut(_translate("MainWindow", "F2"))
        self.pushButton_bot.setText(_translate("MainWindow", "BOT(F1)"))
        self.pushButton_bot.setShortcut(_translate("MainWindow", "F1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
