import sys
from pathlib import Path
from PyQt5.QtWidgets import (QWidget, QApplication, QMainWindow,
                             QTableWidget, QDesktopWidget, QMessageBox,
                             QDateEdit,
                             QWidget, QStackedLayout, QTableWidgetItem)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal
from PyQt5 import uic

from ui.main_page import Ui_MainPage
from ui.login import Ui_Login


class Login(QWidget, Ui_Login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MainWindows(QWidget, Ui_MainPage):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./resource/pin-6-64.ico"))
    window = MainWindows()
    window.show()
    sys.exit(app.exec_())




