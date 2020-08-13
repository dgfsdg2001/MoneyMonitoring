import unittest
import pandas as pd
from account_book.utils import *

class TestUtils(unittest.TestCase):
    def test_to_timestamp(self):
        # Positive cases
        self.assertLess(to_timestamp("2011"), pd.Timestamp.now())
        self.assertLess(to_timestamp("2011-11-12"), pd.Timestamp.now())

        # Negative cases
        with self.assertLogs(level=logging.WARNING):
            self.assertAlmostEqual(to_timestamp("123"), pd.Timestamp.now())


if __name__ == '__main__':
    unittest.main()
