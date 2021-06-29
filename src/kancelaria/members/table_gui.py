# -*- coding: utf-8 -*-

"""
Selected DB tables gui access
"""

from PySide2.QtCore import QSize
from PySide2.QtWidgets import QMainWindow, QWidget, QAction, QListView, QVBoxLayout


class ActivityTblWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Activity Table")
        window = QWidget()
        window.setMinimumSize(QSize(600, 600))
        self.setCentralWidget(window)

        layout = QVBoxLayout()

        alist = QListView(window)
        layout.addWidget(alist)
