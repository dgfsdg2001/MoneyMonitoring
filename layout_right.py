from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import (
    QLayout, QVBoxLayout,
    QLabel, QDateEdit, QTreeView, QPushButton
)


class LayoutRight(QVBoxLayout):
    def __init__(self, parent=None):
        super(LayoutRight, self).__init__(parent)

        self.query = {
            "date": {
                "start": {
                    "title": QLabel("Start Date:"),
                    "value": QDateEdit(QDate.currentDate()),
                },
                "end": {
                    "title": QLabel("Start Date:"),
                    "value": QDateEdit(QDate.currentDate()),
                }
            }
        }

        for k, date in self.query["date"].items():
            date["value"].setCalendarPopup(True)

        self.btn_query = QPushButton("Query")
        self.btn_query.setFixedSize(self.btn_query.sizeHint())
        self.btn_query.clicked.connect(parent.update_data)

        self.addWidget(self.query["date"]["start"]["title"])
        self.addWidget(self.query["date"]["start"]["value"])
        self.addWidget(self.query["date"]["end"]["title"])
        self.addWidget(self.query["date"]["end"]["value"])
        self.addWidget(self.btn_query)
    
        # Test
        tree_view = QTreeView()
        tree_view.setHeaderHidden(True)
        tree_view.setContextMenuPolicy(Qt.CustomContextMenu)
        model = QtGui.QStandardItemModel()

        item1 = QtGui.QStandardItem("Item 1")
        item1.appendRow(QtGui.QStandardItem("Item 1-1"))
        model.appendRow(item1)
        model.appendRow(QtGui.QStandardItem("Item 2"))
        tree_view.setModel(model)

        self.addWidget(QLabel("Details:"))
        self.addWidget(tree_view)

    def update_data(self):
        print("layout_right.py")