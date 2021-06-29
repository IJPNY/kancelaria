# -*- coding: utf-8 -*-

"""
Office application of the Józef Piłsudski Institute of America
"""

import sys
import webbrowser

from PySide2.QtCore import QSize
from PySide2.QtWidgets import (
    QAction,
    QApplication,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QWidget,
)

from PySide2.QtGui import QIcon

from . import __version__, __author__
from .members.home_gui import MembersHomeWindow


class Kancelaria(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        appIcon = QIcon("./src/kancelaria/resources/kancelaria.ico")
        self.setWindowIcon(appIcon)
        self.setWindowTitle("Kancelaria")

        # layout
        layout = QHBoxLayout()
        layout.setContentsMargins(20, 0, 20, 20)
        layout.setSpacing(20)
        layout_left = QVBoxLayout()
        layout_right = QVBoxLayout()

        welcome_msg = QLabel(
            "Witam w Kancelarii,\n\naplikacji biura Instytutu J. Piłsudskiego\n\nw Ameryce"
        )
        layout_left.addWidget(welcome_msg)
        layout.addLayout(layout_left)

        # bulletin button
        btn_bulletin = QPushButton("Bulletin")
        btn_bulletin.setIcon(QIcon("./src/kancelaria/resources/Google-Drive-icon.png"))
        btn_bulletin.setIconSize(QSize(48, 48))
        btn_bulletin.clicked.connect(self.launch_bulletin_widget)
        layout_right.addWidget(btn_bulletin)

        # members db button
        btn_members = QPushButton("Members")
        btn_members.setIcon(QIcon("./src/kancelaria/resources/Photobooth-icon.png"))
        btn_members.setIconSize(QSize(48, 48))
        btn_members.clicked.connect(self.launch_members_widget)
        layout_right.addWidget(btn_members)
        layout.addLayout(layout_right)

        # menu
        # toolbar = QToolBar()
        # self.addToolBar(toolbar)
        action_about = QAction(
            QIcon("./src/kancelaria/resources/lightbulb-icon.png"), "About", self
        )
        action_about.triggered.connect(self.launch_about_widget)
        # toolbar.addAction(action_about)

        action_update = QAction(
            QIcon("./src/kancelaria/resources/hammer-icon.png"), "Updates", self
        )
        action_update.triggered.connect(self.launch_update_widget)

        action_help = QAction(
            QIcon("./src/kancelaria/resources/info-button-icon.png"), "Help", self
        )
        action_help.triggered.connect(self.launch_help)

        action_exit = QAction(
            QIcon("./src/kancelaria/resources/close-icon.png"), "Exit", self
        )
        action_exit.triggered.connect(self.exit_app)

        menu = self.menuBar()
        file_menu = menu.addMenu("File")
        file_menu.addAction(action_about)
        file_menu.addAction(action_update)
        file_menu.addAction(action_help)
        file_menu.addAction(action_exit)

        # wrap up widget
        window = QWidget()
        window.setMinimumSize(QSize(400, 200))
        window.setLayout(layout)
        self.setCentralWidget(window)

    def exit_app(self):
        self.close()

    def launch_about_widget(self):
        QMessageBox.about(
            self,
            "About",
            f"Kancelaria\nVersion {__version__}\nCopyright 2021, {__author__}\nMIT license",
        )

    def launch_update_widget(self):
        print("update widget here.")

    def launch_help(self):
        try:
            webbrowser.open_new("https://github.com/IJPNY/kancelaria")
        except TypeError:
            pass

    def launch_bulletin_widget(self):
        print("Launch here bulletin window.")

    def launch_members_widget(self, s):
        self.widget = MembersHomeWindow()
        self.widget.show()


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    main_window = Kancelaria()
    main_window.show()
    sys.exit(app.exec_())
