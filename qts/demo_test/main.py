from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox
from PyQt5 import uic


class Stats(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("./ui/test.ui")
        self.ui.count_btn.clicked.connect(self.handle_calc)

    def handle_calc(self):
        info = self.textEdit.toPlainText()

        QMessageBox.about(self.window, "结果", f"提示信息 {12}")


if __name__ == "__main__":
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.exec_()




