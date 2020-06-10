import logging
import pandas as pd
from account_book import AccountBook

# logging.basicConfig(filename='example.log',level=logging.DEBUG)
# FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
# logging.basicConfig(format=FORMAT)

if __name__ == '__main__':
    book = AccountBook('MoneyTracking.xlsx')
    print(book.getBalance())
