import datetime
from unittest.mock import patch

import nonstandard as ns


EXAMPLE_DATETIME = datetime.datetime(1954, 3, 11, 16, 4, 52, 38712)


@patch("datetime.datetime")
def test_basic(mock_datetime):
    mock_datetime.now.return_value = EXAMPLE_DATETIME
    assert ns.dense_timestamp() == "19540311160452"


def test_fixed_time():
    time = datetime.datetime(2013, 11, 7, 3, 41, 12, 938529)
    assert ns.dense_timestamp(time) == "20131107034112"


@patch("datetime.datetime")
@patch("random.randrange", return_value=38491039)
def test_unique(mock_randrange, mock_datetime):
    mock_datetime.now.return_value = EXAMPLE_DATETIME
    assert ns.dense_timestamp(unique=True) == "1954031116045238491039"


@patch("datetime.datetime")
def test_decimal(mock_datetime):
    mock_datetime.now.return_value = EXAMPLE_DATETIME
    assert ns.dense_timestamp(decimals=4) == "195403111604520387"


@patch("datetime.datetime")
@patch("random.randrange", return_value=38491039)
def test_decimal_unique(mock_randrange, mock_datetime):
    mock_datetime.now.return_value = EXAMPLE_DATETIME
    assert ns.dense_timestamp(unique=True, decimals=6) == "1954031116045203871238491039"
