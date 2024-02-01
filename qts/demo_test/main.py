from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QPushButton, QPlainTextEdit, QMessageBox,
                             QTableWidget, QTableWidgetItem)
from PyQt5 import uic


class Stats(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("./ui/test02.ui")
        self.init_ui()

    def init_ui(self):
        table = self.ui.tableWidget
        # 设置整行选中
        table.setSelectionBehavior(QTableWidget.SelectRows)
        # 设置表格内容为不可编辑
        table.setEditTriggers(QTableWidget.NoEditTriggers)
        # 行标题隐藏
        table.verticalHeader().setVisible(False)
        # 设置列名字体加粗
        header_font = table.horizontalHeader().font()
        header_font.setBold(True)
        table.horizontalHeader().setFont(header_font)
        if table:
            # 设置表格列数
            table.setColumnCount(3)

            # 设置列名
            column_headers = ['姓名', '年龄', '城市']
            table.setHorizontalHeaderLabels(column_headers)

            data = [['Alice', '25', 'New York'],
                    ['Bob', '30', 'San Francisco'],
                    ['Charlie', '22', 'Los Angeles weihule lianghao luozhisun'],
                    ['Charlie', '22', 'Los Angeles'],
                    ['Charlie', '22', 'Los Angeles'],
                    ['Charlie', '22', 'Los Angeles'],
                    ['Charlie', '22', 'Los Angeles']]
            for row_idx, row_data in enumerate(data):
                table.insertRow(row_idx)
                # for col, value in enumerate()
                for col_idx, value in enumerate(row_data):
                    item = QTableWidgetItem(value)
                    table.setItem(row_idx, col_idx, item)

            total_width = table.width()
            print(total_width)
            table.setColumnWidth(0, 50)
            table.setColumnWidth(1, 50)
            last_column_index = table.columnCount() - 1
            last_column_width = total_width - sum(table.columnWidth(i) for i in range(last_column_index))
            print(f"last_column_index = {last_column_index} last_column_width = {last_column_width}")
            table.setColumnWidth(last_column_index, last_column_width)


if __name__ == "__main__":
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.exec_()




