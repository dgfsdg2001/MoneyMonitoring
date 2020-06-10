import json
import xlrd
import logging
import pandas as pd
from os.path import dirname

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


class XlsMapping():
    def __init__(self, xls: xlrd.book.Book, formats_json=None):
        self.xls = xls
        if formats_json is None:
            formats_json = '{}\\xls_format.json'.format(dirname(__file__))

        with open(formats_json, encoding='UTF-8') as file:
            self.mappings = json.load(file)

        self.data_range = pd.read_excel(
            self.xls,
            sheet_name=self.mappings['data_range_sheet']['sheet_name'])

    def get_df(self, mapping, bc_list):
        mapping_bc = mapping['basic_columns']

        # Map arbitary column names in xls to fixed names used in DataFrame.
        df = (
            pd.read_excel(self.xls, sheet_name=mapping['sheet_name'])
            .rename(columns={mapping_bc[k]['name']: k for k in bc_list})
        )
        if 'optional_columns' in mapping:
            df = df.rename(
                columns={
                    v['name']: k
                    for k, v in mapping['optional_columns'].items()})

        # Validate whether values belong to the pre-defiend set.
        def is_not_in_range(sub_mapping):
            for k, v in sub_mapping.items():
                if 'data_range' not in v:
                    continue
                if not set(df[k]) <= set(self.data_range[v['data_range']]):
                    return True
            return False

        if is_not_in_range(mapping_bc):
            logger.warning(
                'Mismatched Data Range at {}.{}(sheet.column_name).'
                .format(mapping['sheet_name'], v['name']))
        if ('optional_columns' in mapping
                and is_not_in_range(mapping['optional_columns'])):
            logger.warning(
                'Mismatched Data Range at {}.{}(sheet.column_name).'
                .format(mapping['sheet_name'], v['name']))
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
                'date',
                'from_bank', 'from_account', 'from_currency', 'from_amount',
                'to_bank', 'to_account', 'to_currency', 'to_amount'])
