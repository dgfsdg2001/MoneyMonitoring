import sys
import os
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, qApp, QMainWindow, QWidget, QAction,
    QFileDialog, QErrorMessage,
    QLayout, QGridLayout,
    )
from layout_top import LayoutTop
from layout_left import LayoutLeft
from layout_right import LayoutRight
from account_book import AccountBook

class AccountBookWrapper(AccountBook):
    def __init__(self, filepath):
        super(AccountBookWrapper, self).__init__(filepath)
        self.start_time = self.DEFAULT_START_TIME
        self.end_time = self.DEFAULT_END_TIME

    def set_query_interval(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def get_balance(self)
    

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle(__name__)
        self.book = None
        self.layout_top = LayoutTop(self)
        self.layout_left = LayoutLeft(self)
        self.layout_right = LayoutRight(self)

        # Main layout
        layout_main = QGridLayout()
        layout_main.addLayout(
            self.layout_top, 0, 0, 1, 2, Qt.AlignTop | Qt.AlignLeft)
        layout_main.addLayout(
            self.layout_left, 1, 0, Qt.AlignTop | Qt.AlignLeft)
        layout_main.addLayout(
            self.layout_right,1, 1, Qt.AlignTop | Qt.AlignLeft)

        # Central widget
        widget = QWidget()
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)

        # Menubar
        main_menu = self.menuBar()

        action_openFile = QAction("&Open File", self)
        action_openFile.setShortcut("Ctrl+O")
        action_openFile.setStatusTip('Open File')
        action_openFile.triggered.connect(self.oepn_file)

        action_exit = QAction("&Exit", self)
        action_exit.setShortcut("Ctrl+Q")
        action_exit.setStatusTip('Exit program')
        action_exit.triggered.connect(self.close)

        # Sub-menu File
        file_menu = main_menu.addMenu("&File")
        file_menu.addAction(action_openFile)
        file_menu.addAction(action_exit)

    def oepn_file(self):
        filename = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd())[0]
        try:
            self.book = AccountBook(filename)
            self.update_data()
        except:
            err = QErrorMessage()
            err.showMessage("Open {} failed. {}".format(filename, sys.exc_info()[1]))
            err.exec_()

    def update_data(self, obj=None):
        if self.book is not None:
        self.layout_top.update_data()
        self.layout_left.update_data() 
        self.layout_right.update_data()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
