import datetime
from unittest.mock import patch

import nonstandard as ns


EXAMPLE_DATETIME = datetime.datetime(1954, 3, 11, 16, 4, 52, 38712)


@patch("datetime.datetime")
def test_basic(mock_datetime):
    mock_datetime.now.return_value = EXAMPLE_DATETIME
    assert ns.safe_timestamp() == "1954_03_11_16_04_52"


def test_fixed_time():
    time = datetime.datetime(2013, 11, 7, 3, 41, 12, 938529)
    assert ns.safe_timestamp(time) == "2013_11_07_03_41_12"


@patch("datetime.datetime")
@patch("random.randrange", return_value=38491039)
def test_unique(mock_randrange, mock_datetime):
    mock_datetime.now.return_value = EXAMPLE_DATETIME
    assert ns.safe_timestamp(unique=True) == "1954_03_11_16_04_52_38491039"


@patch("datetime.datetime")
def test_decimal(mock_datetime):
    mock_datetime.now.return_value = EXAMPLE_DATETIME
    assert ns.safe_timestamp(decimals=4) == "1954_03_11_16_04_52_0387"


@patch("datetime.datetime")
@patch("random.randrange", return_value=38491039)
def test_decimal_unique(mock_randrange, mock_datetime):
    mock_datetime.now.return_value = EXAMPLE_DATETIME
    assert ns.safe_timestamp(unique=True, decimals=6) == "1954_03_11_16_04_52_038712_38491039"


@patch("datetime.datetime")
@patch("random.randrange", return_value=38491039)
def test_double_separator(mock_randrange, mock_datetime):
    mock_datetime.now.return_value = EXAMPLE_DATETIME
    assert ns.safe_timestamp(unique=True, decimals=6, double_separator=True) == "1954_03_11__16_04_52_038712__38491039"
