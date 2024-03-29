import datetime
from unittest.mock import patch

import nonstandard as ns


EXAMPLE_DATETIME = datetime.datetime(1954, 3, 11, 16, 4, 52, 38712)


@patch("datetime.datetime")
def test_basic(mock_datetime):
    mock_datetime.now.return_value = EXAMPLE_DATETIME
    assert ns.readable_timestamp() == "1954-03-11 16:04:52"


def test_fixed_time():
    time = datetime.datetime(2013, 11, 7, 3, 41, 12, 938529)
    assert ns.readable_timestamp(time) == "2013-11-07 03:41:12"


@patch("datetime.datetime")
@patch("random.randrange", return_value=38491039)
def test_unique(mock_randrange, mock_datetime):
    mock_datetime.now.return_value = EXAMPLE_DATETIME
    assert ns.readable_timestamp(unique=True) == "1954-03-11 16:04:52 38491039"


@patch("datetime.datetime")
def test_decimal(mock_datetime):
    mock_datetime.now.return_value = EXAMPLE_DATETIME
    assert ns.readable_timestamp(decimals=4) == "1954-03-11 16:04:52.0387"


@patch("datetime.datetime")
@patch("random.randrange", return_value=38491039)
def test_decimal_unique(mock_randrange, mock_datetime):
    mock_datetime.now.return_value = EXAMPLE_DATETIME
    assert ns.readable_timestamp(unique=True, decimals=6) == "1954-03-11 16:04:52.038712 38491039"
