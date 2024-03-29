import nonstandard as ns
import pytest


def test_singleton():
    assert ns.unwrap([6]) == 6


def test_element():
    assert ns.unwrap(9) == 9


def test_string():
    assert ns.unwrap("hat") == "hat"


def test_nested():
    inner_list = ["granite", 5]
    assert ns.unwrap([inner_list]) is inner_list


def test_empty():
    with pytest.raises(ValueError, match="Tried to unwrap a collection containing no items."):
        ns.unwrap([])


def test_not_singleton():
    with pytest.raises(ValueError, match="Tried to unwrap a collection containing more than one item."):
        ns.unwrap([6, 6])


def test_generator():
    def sample_generator():
        yield 12

    assert ns.unwrap(sample_generator()) == 12


def test_bytes():
    with pytest.raises(ValueError, match="Uncertain whether to treat bytes as an item or collection in unwrap."):
        assert ns.unwrap(b"hat")
