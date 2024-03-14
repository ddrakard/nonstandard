import pytest
from nonstandard import collections


def test_singleton():
    assert collections.unwrap([6]) == 6


def test_element():
    assert collections.unwrap(9) == 9


def test_string():
    assert collections.unwrap("hat") == "hat"


def test_nested():
    inner_list = ["granite", 5]
    assert collections.unwrap([inner_list]) is inner_list


def test_empty():
    with pytest.raises(ValueError, match="Tried to unwrap a collection containing no items."):
        collections.unwrap([])


def test_not_singleton():
    with pytest.raises(ValueError, match="Tried to unwrap a collection containing more than one item."):
        collections.unwrap([6, 6])


def test_generator():
    def sample_generator():
        yield 12

    assert collections.unwrap(sample_generator()) == 12


def test_bytes():
    with pytest.raises(ValueError, match="Uncertain whether to treat bytes as an item or collection in unwrap."):
        assert collections.unwrap(b"hat")
