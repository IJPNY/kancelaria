# -*- coding: utf-8 -*-

"""
Data models
"""

from QtCore import Qt, QAbstractListModel


class NameList(QAbstractListModel):
    def __init__(self, *args, names=None, **kwargs):
        super(NameList, self).__init__(*args, **kwargs)
        self.names = names or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            status, text = self.names[index.row()]
            return text

    def rowCount(self, index):
        return len(self.names)
