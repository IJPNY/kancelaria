# -*- coding: utf-8 -*-

"""
GUI for members database app
"""

from PySide2.QtCore import QSize
from PySide2.QtWidgets import QMainWindow, QWidget, QAction


from .table_gui import ActivityTblWindow


class MembersHomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Members Database")
        window = QWidget()
        window.setMinimumSize(QSize(600, 600))
        self.setCentralWidget(window)

        # menu
        action_home = QAction("Home", self)
        action_home.triggered.connect(self.widget_browse)

        # tables submenu actions
        action_activity = QAction("Activity Table", self)
        action_activity.triggered.connect(self.widget_activity_tbl)

        action_bulletin = QAction("Bulletin Category Table", self)
        action_bulletin.triggered.connect(self.widget_bulletin_tbl)

        action_city = QAction("City Table", self)
        action_city.triggered.connect(self.widget_city_tbl)

        action_contribution = QAction("Contribution Type Table", self)
        action_contribution.triggered.connect(self.widget_contribution_tbl)

        menu = self.menuBar()

        # file menu
        file_menu = menu.addMenu("File")
        file_menu.addAction(action_home)
        tables_submenu = file_menu.addMenu("Tables")
        tables_submenu.addAction(action_activity)
        tables_submenu.addAction(action_bulletin)
        tables_submenu.addAction(action_city)
        tables_submenu.addAction(action_contribution)

        # exit action
        action_close = QAction("Close", self)
        action_close.triggered.connect(self.close_widget)

        file_menu.addAction(action_close)

        # reports menu
        report_menu = menu.addMenu("Reports")

        # help menu
        help_menu = menu.addMenu("Help")

    def close_widget(self):
        self.close()

    def widget_browse(self):
        pass

    def widget_activity_tbl(self):
        self.activity_window = ActivityTblWindow()
        self.activity_window.show()

    def widget_bulletin_tbl(self):
        pass

    def widget_city_tbl(self):
        pass

    def widget_contribution_tbl(self):
        pass
