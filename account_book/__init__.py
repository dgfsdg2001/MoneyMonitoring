import xlrd
import logging
import pandas as pd
from account_book.xls_mapping import XlsMapping

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


class AccountBook():
    def __init__(self, excel_file):

        xls_mapping = XlsMapping(xlrd.open_workbook(excel_file))

        # Read sheets to DataFrame
        self.spending = xls_mapping.get_spending()
        self.income = xls_mapping.get_income()
        self.transfer = xls_mapping.get_transfer()

    def getBalance(self) -> dict():
        spending = self.spending
        income = self.income
        transfer = self.transfer

        currencies = (
            set(spending['currency']) |
            set(income['currency']) |
            set(transfer['to_currency']) |
            set(transfer['from_currency']))

        balances = dict()
        for currency in currencies:
            money_in = (
                income.loc[income['currency'] == currency]['amount'].sum()
                + transfer.loc[transfer['to_currency'] == currency]['to_amount'].sum())

            money_out = (
                spending.loc[spending['currency'] == currency]['amount'].sum()
                + transfer.loc[transfer['from_currency'] == currency]['from_amount'] .sum())

            balances[currency] = money_in - money_out

        logger.error(balances)

        return balances
