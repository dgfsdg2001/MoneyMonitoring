import json
import xlrd
import pandas as pd
from os.path import dirname


class XlsMapping():
    def __init__(self, xls: xlrd.book.Book, formats_json=None):
        self.xls = xls
        if formats_json is None:
            formats_json = '{}\\xls_format.json'.format(dirname(__file__))

        with open(formats_json, encoding='UTF-8') as file:
            self.mappings = json.load(file)

    def get_df(self, mapping, bc_list):
        mapping_bc = mapping['basic_columns']
        df = (
            pd.read_excel(self.xls, sheet_name=mapping['sheet_name'])
            .rename(columns={mapping_bc[k]['name']: k for k in bc_list})
        )
        if 'optional_columns' in mapping:
            df = df.rename(
                columns={
                    v['name']: k
                    for k, v in mapping['optional_columns'].items()})
        return df

    def get_spending(self) -> pd.DataFrame:
        return self.get_df(
            mapping=self.mappings['spending'],
            bc_list=[
                'date', 'currency', 'bank', 'account', 'amount',
                'category'])

    def get_income(self) -> pd.DataFrame:
        return self.get_df(
            mapping=self.mappings['income'],
            bc_list=[
                'date', 'currency', 'bank', 'account', 'amount',
                'category'])

    def get_transfer(self) -> pd.DataFrame:
        return self.get_df(
            mapping=self.mappings['transfer'],
            bc_list=[
                'date', 'currency', 'from_bank', 'from_account',
                'to_bank', 'to_account', 'amount'])
