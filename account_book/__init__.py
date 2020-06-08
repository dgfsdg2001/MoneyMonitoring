import xlrd
import pandas as pd
from account_book.xls_mapping import XlsMapping


class AccountBook():
    def __init__(self, excel_file):

        xls_mapping = XlsMapping(xlrd.open_workbook(excel_file))

        # Read sheets to DataFrame
        self.spending = xls_mapping.get_spending()
        self.income = xls_mapping.get_income()
        self.transfer = xls_mapping.get_transfer()

        print(self.spending)
        print(self.income)
        print(self.transfer)
