import logging
import pandas as pd
from account_book import AccountBook

# logging.basicConfig(filename='example.log',level=logging.DEBUG)
# FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
# logging.basicConfig(format=FORMAT)

if __name__ == '__main__':
    book = AccountBook('MoneyTracking.xlsx')
    print('Total balance:     ', book.get_balance(currencies=['USD']))
    print('June 2020 balance: ', book.get_balance(start_time='2020-06-01'))
    print('June 2020 income:  ', book.get_income(start_time='2020-06-01'))
    print('June 2020 spending:', book.get_spending(start_time='2020-06-01'))
