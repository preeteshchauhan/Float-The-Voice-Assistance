from mainwindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QTimer,QTime,QDate
from PyQt5.uic import loadUiType
import float
import webbrowser as web
import sys


class MainThread(QThread):

    def __init__(self):

        super(MainThread,self).__init__()

    def run(self):
        float.Task_Gui()

startExe = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):

        super().__init__()

        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.browser.clicked.connect(self.browser_app)
        self.gui.whatsapp.clicked.connect(self.whatsapp_app)
        self.gui.youtube.clicked.connect(self.youtube_app)

    def browser_app(self):
        web.open("https://www.google.com/")

    def youtube_app(self):
        web.open("https://www.youtube.com/")

    def whatsapp_app(self):
        web.open("https://web.whatsapp.com/")

    def startTask(self):
    

        self.gui.label = QtGui.QMovie("://images//untitled-4.gif")
        self.gui.gif.setMovie(self.gui.label)
        self.gui.label.start()

        startExe.start()

GuiApp = QApplication(sys.argv)
exit(GuiApp.exec_())

