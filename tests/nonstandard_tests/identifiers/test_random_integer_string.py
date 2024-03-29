from unittest.mock import patch

import pytest
from nonstandard import random_integer_string


@patch("random.randrange")
def test_length_6(mock_randrange):
    mock_randrange.return_value = 739194
    assert random_integer_string(6) == "739194"
    mock_randrange.assert_called_with(100000, 1000000)


def test_zero_length():
    assert random_integer_string(0) == ""


def test_negative_length():
    with pytest.raises(ValueError, match="Call to random_integer_string with negative length."):
        random_integer_string(-3)
