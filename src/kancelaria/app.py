# -*- coding: utf-8 -*-

"""
Office application of the Józef Piłsudski Institute of America
"""

import sys
from PySide2 import QtWidgets


class Kancelaria(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("kancelaria")
        self.label = QtWidgets.QLabel("Witam w Kancelarii!")
        self.label.show()
        self.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = Kancelaria()
    sys.exit(app.exec_())
