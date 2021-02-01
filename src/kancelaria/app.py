# -*- coding: utf-8 -*-

"""
Office application of the Józef Piłsudski Institute of America
"""

import sys
from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QToolBar, QAction


class Kancelaria(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("kancelaria")
        self.setWindowIcon(QtGui.QIcon("src/kancelaria/resources/kancelaria.ico"))

        # exit app
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(48, 48))
        self.addToolBar(toolbar)

        exit_action = QAction(
            QtGui.QIcon("src/kancelaria/resources/exit-icon-32.png"), "Zakończ", self
        )
        exit_action.triggered.connect(self.exit_app)
        exit_action.setCheckable(True)
        toolbar.addAction(exit_action)

        bulletin_action = QAction(
            QtGui.QIcon("src/kancelaria/resources/notebook-icon-48.png"),
            "Biuletyn",
            self,
        )
        bulletin_action.triggered.connect(self.bulletin)
        toolbar.addAction(bulletin_action)

        members_action = QAction(
            QtGui.QIcon("src/kancelaria/resources/contact-icon-48.png"),
            "Baza członków",
            self,
        )
        members_action.triggered.connect(self.members)
        toolbar.addAction(members_action)

        self.show()

    def exit_app(self):
        pass

    def bulletin(self):
        pass

    def members(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("xpnative")
    main_window = Kancelaria()
    sys.exit(app.exec_())
