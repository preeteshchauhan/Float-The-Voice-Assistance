from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow

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
