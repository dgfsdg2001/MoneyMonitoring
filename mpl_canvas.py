import matplotlib

matplotlib.use("Qt5Agg")


class MplCanvas(matplotlib.backends.backend_qt5agg.FigureCanvasQTAgg):
    def __init__(self, parent=None):
        fig = matplotlib.figure.Figure()
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)