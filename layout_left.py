from PyQt5.QtWidgets import (
    QLayout, QVBoxLayout,
    QLabel
)
from mpl_canvas import MplCanvas

class LayoutLeft(QVBoxLayout):
    def __init__(self, parent=None):
        super(LayoutLeft, self).__init__(parent)
        
        self.plot = MplCanvas(self)

        # Test
        import pandas as pd
        df = pd.DataFrame(
            {'mass': [0.330, 4.87, 5.97], 'radius': [2439.7, 6051.8, 6378.1]},
            index=['Mercury', 'Venus', 'Earth'])
        # df.plot.pie(y='mass', ax=sc.axes)
        df.plot.pie(subplots=True, ax=self.plot.axes)
        self.addWidget(self.plot)

    def update_data(self):
        print("layout_left.py")