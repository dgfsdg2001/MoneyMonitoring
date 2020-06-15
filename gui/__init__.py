import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLayout, QGridLayout,
    )
from layout_top import LayoutTop
from layout_left import LayoutLeft
from layout_right import LayoutRight

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle(__name__)

            
        layout_top = LayoutTop()
        layout_left = LayoutLeft()
        layout_right = LayoutRight()

        # Main layout
        layout_main = QGridLayout()
        layout_main.addLayout(layout_top, 0, 0, 1, 2, Qt.AlignTop | Qt.AlignLeft)
        layout_main.addLayout(layout_left, 1, 0, Qt.AlignTop | Qt.AlignLeft)    # row=1, col=0
        layout_main.addLayout(layout_right, 1, 1, Qt.AlignTop | Qt.AlignLeft)   # row=1, col=1

        # Central widget
        widget = QWidget()
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
