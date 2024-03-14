from collections import abc
from typing import Any


def unwrap(value: Any) -> Any:
    """
    Return the item inside `value` if it is a singleton collection,
    and return `value` itself if it is not a collection.
    If it is a non-singleton collection, and exception is raised.

    Strings are not treated as collections, because it is
    often desirable to unwrap collections where strings are the items,
    and unwrapping a singleton string has no effect.
    """
    if isinstance(value, (bytes, bytearray)):
        raise ValueError("Uncertain whether to treat bytes as an item or collection in unwrap.")
    if isinstance(value, str) or not isinstance(value, abc.Iterable):
        return value
    iterator = iter(value)
    try:
        item = next(iterator)
    except StopIteration:
        raise ValueError("Tried to unwrap a collection containing no items.")
    try:
        # Attempt to get a second item, if successful then the collection is not a singleton.
        next(iterator)
        raise ValueError("Tried to unwrap a collection containing more than one item.")
    except StopIteration:
        # No second item, `value` is a singleton.
        return item
