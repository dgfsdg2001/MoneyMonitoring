import logging
import pandas as pd

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


def to_timestamp(str: str) -> pd.Timestamp:
    """
    Transfrom date time string to pandas.Timestamp object. Return
    current time if the input string is malformatted.

    Args:
        str: date time string

    Returns:
        pandas.Timestamp
    """
    try:
        return pd.Timestamp(str)
    except (TypeError, ValueError) as e:
        logger.warning("{}, return currecnt time".format(e))
        return pd.Timestamp.now()


def amount_within_period(
        df: pd.DataFrame,
        currency: str,
        start_time: pd.Timestamp, end_time: pd.Timestamp) -> float:
    """
    Get total amount within a given period of time.

    Args:
        currency: currency string
        start_date:
        end_date:

    Returns:
        total amount
    """
    return df.loc[
        (start_time <= df['date']) &
        (df['date'] <= end_time) &
        (df['currency'] == currency)]['amount'].sum()
