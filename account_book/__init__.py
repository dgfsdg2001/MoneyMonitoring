import xlrd
import logging

import pandas as pd
from account_book.xls_mapping import XlsMapping
from account_book.utils import to_timestamp, amount_within_period

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


class AccountBook():
    DEFAULT_START_TIME = '1900-01-01'
    DEFAULT_END_TIME = '2200-12-31'

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
            return (
                set(self.spending[name])
                | set(self.income[name])
                | set(self.transfer_in[name])
                | set(self.transfer_out[name]))

        self.currencies = get_unique_values('currency')
        self.banks = get_unique_values('bank')
        self.accounts = get_unique_values('account')

        self.spending_categories = set(self.spending['category'])
        self.income_categories = set(self.income['category'])

    def get_income(
            self,
            start_time: str = DEFAULT_START_TIME,
            end_time: str = DEFAULT_END_TIME,
            currencies: list = None) -> dict:
        """
        Get total income within a given period of time.

        Args:
            start_date: datetime string in ISO format
            end_date: datetime string in ISO format
            currencies: list of currencies

        Returns:
            dict[currency] = total income
        """
        income = dict()
        currencies = self.currencies if currencies is None else currencies
        for currency in filter(lambda x: x in currencies, self.currencies):
            income[currency] = amount_within_period(
                self.income, currency,
                to_timestamp(start_time), to_timestamp(end_time))

        return income

    def get_spending(
            self,
            start_time: str = DEFAULT_START_TIME,
            end_time: str = DEFAULT_END_TIME,
            currencies: list = None) -> dict:
        """
        Get total spending within a given period of time.

        Args:
            start_date: datetime string in ISO format
            end_date: datetime string in ISO format
            currencies: list of currencies

        Returns:
            dict[currency] = total spending
        """
        spending = dict()
        currencies = self.currencies if currencies is None else currencies
        for currency in filter(lambda x: x in currencies, self.currencies):
            spending[currency] = amount_within_period(
                self.spending, currency,
                to_timestamp(start_time), to_timestamp(end_time))

        return spending

    def get_transfer_out(
            self,
            start_time: str = DEFAULT_START_TIME,
            end_time: str = DEFAULT_END_TIME,
            currencies: list = None) -> dict:
        """
        Get total transfer-out within a given period of time.

        Args:
            start_date: datetime string in ISO format
            end_date: datetime string in ISO format
            currencies: list of currencies

        Returns:
            dict[currency] = total transfer-out
        """
        transfer_out = dict()
        currencies = self.currencies if currencies is None else currencies
        for currency in filter(lambda x: x in currencies, self.currencies):
            transfer_out[currency] = amount_within_period(
                    self.income, currency,
                    to_timestamp(start_time), to_timestamp(end_time))

        return transfer_out

    def get_transfer_in(
            self,
            start_time: str = DEFAULT_START_TIME,
            end_time: str = DEFAULT_END_TIME,
            currencies: list = None) -> dict:
        """
        Get total transfer-in within a given period of time.

        Args:
            start_date: datetime string in ISO format
            end_date: datetime string in ISO format
            currencies: list of currencies

        Returns:
            dict[currency] = total transfer-in
        """
        transfer_in = dict()
        currencies = self.currencies if currencies is None else currencies
        for currency in filter(lambda x: x in currencies, self.currencies):
            transfer_in[currency] = amount_within_period(
                self.income, currency,
                to_timestamp(start_time), to_timestamp(end_time))

        return transfer_in

    def get_balance(
            self,
            start_time: str = DEFAULT_START_TIME,
            end_time: str = DEFAULT_END_TIME,
            currencies: list = None) -> dict():
        """
        Get total balance within a given period of time.

        Args:
            start_date: datetime string in ISO format
            end_date: datetime string in ISO format
            currencies: list of currencies

        Returns:
            dict[currency] = balance
        """

        balances = dict()
        income = self.get_income(start_time, end_time, currencies)
        spending = self.get_spending(start_time, end_time, currencies)
        transfer_in = self.get_transfer_in(start_time, end_time, currencies)
        transfer_out = self.get_transfer_in(start_time, end_time, currencies)

        currencies = self.currencies if currencies is None else currencies
        for currency in filter(lambda x: x in currencies, self.currencies):
            balances[currency] = (
                income.get(currency, 0)
                + transfer_in.get(currency, 0)
                - spending.get(currency, 0)
                - transfer_out.get(currency, 0))

        return balances
