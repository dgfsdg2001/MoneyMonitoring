from PyQt5.QtWidgets import (
    QLayout, QGridLayout,
    QLabel
)

class LayoutTop(QGridLayout):
    def __init__(self, parent=None):
        super(LayoutTop, self).__init__(parent)
        self.setSizeConstraint(QLayout.SetFixedSize)

        self.lables = {
            "balance": {
                "title": QLabel("Balance:"),
                "value": QLabel("0.0")
            },
            "income_spending": {
                "title": QLabel("Income/Spending:"),
                "value": QLabel("0.0/0.0")
            },
            "transfer_in_out": {
                "title": QLabel("Transfer In/Out:"),
                "value": QLabel("0.0/0.0")
            },
        }
        
        row = 0
        for key in ["balance", "income_spending", "transfer_in_out"]:
            self.addWidget(self.lables[key]['title'], row, 0)
            self.addWidget(self.lables[key]['value'], row, 1)
            row += 1

