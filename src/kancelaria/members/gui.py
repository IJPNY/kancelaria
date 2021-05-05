# -*- coding: utf-8 -*-

"""
GUI for members database app
"""

from PySide2.QtCore import QSize
from PySide2.QtWidgets import QMainWindow, QWidget


class MembersWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Baza członków")
        window = QWidget()
        window.setMinimumSize(QSize(600, 600))
        self.setCentralWidget(window)
