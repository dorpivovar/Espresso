import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt
from PyQt5 import uic

GROUND_OR_GRAINS = {
    0: 'молотый',
    1: 'в зёрнах'
}
GROUND_OR_GRAINS_NUMBER = 3


class CoffeeMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.coffee_table = self.findChild(QTableWidget, 'coffee_table')
        self.coffee_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.load_table()

    def load_table(self):
        self.coffee_table.setRowCount(0)
        with sqlite3.connect('coffee.sqlite3') as con:
            cur = con.cursor()
            cur.execute('SELECT * FROM coffee')
            data = cur.fetchall()
            self.coffee_table.setRowCount(len(data))
            for i, row in enumerate(data):
                for j, value in enumerate(row):
                    if j == GROUND_OR_GRAINS_NUMBER:
                        value = GROUND_OR_GRAINS.get(value, str(value))
                    item = QTableWidgetItem(str(value))
                    item.setFlags(Qt.ItemIsEnabled)
                    self.coffee_table.setItem(i, j, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CoffeeMainWindow()
    window.show()
    sys.exit(app.exec())
