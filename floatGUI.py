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
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit


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

class Assistant(QObject):
    def __init__(self):
        super().__init__()

    def process_input(self, text):
        # Process user's input and return assistant's response
        return "Hello, I am your smart voice assistant."

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart Voice Assistant")

        # Create the QTextEdit widget
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)

        # Connect the textChanged signal to the process_input slot
        self.text_edit.textChanged.connect(self.process_input)

        # Create an instance of the Assistant class
        self.assistant = Assistant()

    def process_input(self):
        # Get the user's input
        text = self.text_edit.toPlainText()

        # Process the input using the Assistant class
        response = self.assistant.process_input(text)

        # Display the response in the QTextEdit widget
        self.text_edit.setText(response)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the UI from the .ui file created in Designer
        self.setupUi(self)

        # Create a QTimer to update the QDateTimeEdit widget every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000)

    def updateDateTime(self):
        # Get the current date and time
        currentDateTime = QDateTime.currentDateTime()

        # Update the QDateTimeEdit widget with the current date and time
        self.dateTimeEdit.setDateTime(currentDateTime)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
 
