import xlrd
import logging
import pandas as pd
from datetime import datetime
from account_book.xls_mapping import XlsMapping

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


class AccountBook():
    def __init__(self, excel_filepath):
        """
        Constructor of class AccountBook.

        Args: 
            excel_filepath: path to the input xls file.

        Raises:
            TODO
        """
        xls_mapping = XlsMapping(xlrd.open_workbook(excel_filepath))
        self.spending = xls_mapping.get_spending()
        self.income = xls_mapping.get_income()
        self.transfer_in = xls_mapping.get_transfer_in()
        self.transfer_out = xls_mapping.get_transfer_out()

        def get_unique_values(name):
            return (set(self.spending[name]) | 
                        set(self.income[name])   |
                        set(self.transfer_in[name]) | 
                        set(self.transfer_out[name]))

        self.currencies = get_unique_values('currency')
        self.banks = get_unique_values('bank')
        self.accounts = get_unique_values('account')

        self.spending_categories = set(self.spending['category'])
        self.income_categories = set(self.income['category'])

    # TODO: refactor with getIncome(), getSpending(), get_transfer_in() and get_transfer_out()
    def getBalance(self, start_time=None, end_time=None, currencies: list =[]) -> dict():
        """
        Get balance for a set of categories within a given time.

        Args:
            start_date: string in ISO formt
            end_date: string in ISO format
            currency:
            category:

        Returns:
            dict

        Raises:
        """
        balances = dict()
        try:
            start_time = pd.Timestamp(start_time) if start_time is not None else pd.Timestamp.min 
            end_time = pd.Timestamp(end_time) if end_time is not None else pd.Timestamp.now()
            
        except ValueError or TypeError as e:
            logger.error('Invalid args: start_time={}, end_time={}'
                            .format(start_time, end_time))
            return balances
        
        for currency in filter(lambda x: x in currencies, self.currencies):
            def amount_within_range(df):
                return df.loc[
                    (start_time <= df['date']) & 
                    (df['date'] <= end_time) & 
                    (df['currency'] == currency)]['amount'].sum()
            
            balances[currency] = (
                amount_within_range(self.income) + 
                amount_within_range(self.transfer_in) +
                amount_within_range(self.spending) -
                amount_within_range(self.transfer_out))

        return balances
