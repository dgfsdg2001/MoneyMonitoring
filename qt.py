import sys
import matplotlib
from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLayout, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QToolBar, QAction, QStatusBar, QStyle, QDateEdit,
    QTreeView
    )
from PyQt5.QtCore import Qt, QDate

matplotlib.use("Qt5Agg")


class MplCanvas(matplotlib.backends.backend_qt5agg.FigureCanvasQTAgg):
    def __init__(self, parent=None):
        fig = matplotlib.figure.Figure()
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle(__name__)

        # Top layout
        layout_top = QHBoxLayout()
        balance = QLabel("0.0")
        income = QLabel("0.0")
        spending = QLabel("0.0")
        # title_font = QtGui.QFont("Time", 18, QtGui.QFont.Bold)
        # balance.setFont(title_font)
        layout_top.addWidget(QLabel("Income:"))
        layout_top.addWidget(balance)
        layout_top.addWidget(QLabel("Spending:"))
        layout_top.addWidget(income)
        layout_top.addWidget(QLabel("Balance:"))
        layout_top.addWidget(spending)
        layout_top.setSizeConstraint(QLayout.SetFixedSize)

        # Left layout
        layout_left = QVBoxLayout()
        sc = MplCanvas(self)

        # Testing
        import pandas as pd
        df = pd.DataFrame(
            {'mass': [0.330, 4.87, 5.97], 'radius': [2439.7, 6051.8, 6378.1]},
            index=['Mercury', 'Venus', 'Earth'])
        # df.plot.pie(y='mass', ax=sc.axes)
        df.plot.pie(subplots=True, ax=sc.axes)
        layout_left.addWidget(sc)

        # Right layout
        layout_right = QVBoxLayout()
        query_start_time = QDateEdit(QDate.currentDate())
        query_end_time = QDateEdit(QDate.currentDate())

        layout_right.addWidget(QLabel("Start Date:"))
        layout_right.addWidget(query_start_time)
        layout_right.addWidget(QLabel("End Date:"))
        layout_right.addWidget(query_end_time)

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

        layout_right.addWidget(QLabel("Details:"))
        layout_right.addWidget(tree_view)

        # Main layout
        layout_main = QGridLayout()
        layout_main.addLayout(layout_top, 0, 0, 1, 2, Qt.AlignTop | Qt.AlignLeft)
        layout_main.addLayout(layout_left, 1, 0, Qt.AlignTop | Qt.AlignLeft)    # row=1, col=0
        layout_main.addLayout(layout_right, 1, 1, Qt.AlignTop | Qt.AlignLeft)   # row=1, col=1

        # Central widget
        widget = QWidget()
        widget.setLayout(layout_main)
        self.setCentralWidget(widget)

        # Tool & status bar
        self.setStatusBar(QStatusBar(self))
        toolbar = QToolBar("My tool bar")
        toolbar.setContextMenuPolicy(Qt.PreventContextMenu)  # disable right clicking
        self.addToolBar(toolbar)

        button_action = QAction("Your button", self)   # Pass itself as parent of QAction
        button_action.setStatusTip("This is a button")
        button_action.triggered.connect(self.clicked)
        button_action.setCheckable(True)
        button_action.setIcon(self.style().standardIcon(getattr(QStyle, "SP_MediaPlay")))
        toolbar.addAction(button_action)

        button_action_2 = QAction("Your button 2", self)   # Pass itself as parent of QAction
        button_action_2.setStatusTip("This is a button")
        button_action_2.triggered.connect(self.clicked)
        button_action_2.setCheckable(True)
        button_action_2.setIcon(self.style().standardIcon(getattr(QStyle, "SP_ArrowForward")))
        toolbar.addAction(button_action_2)

    def clicked(self, s):
        print("clicked ", s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
