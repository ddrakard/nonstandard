import datetime
import hashlib
import random
import typing
from string import ascii_letters
from string import digits


def is_safe_identifier(string: str, allowed_symbols: typing.Iterable[str] = ("_",)) -> bool:
    """
    Check whether the string is a "safe" identifier - it contains only alphanumeric characters
    and allowed symbols (only underscores by default) and is not empty.

    Args:
        string: The string to check.
        allowed_symbols: The symbols to allow in addition to alphanumeric characters.
    """
    safe_characters = ascii_letters + digits + "".join(allowed_symbols)
    return len(string) > 0 and all(character in safe_characters for character in string)


def identifierise(string: str, replacement_character: str = "_", allowed_symbols: typing.Iterable[str] = ()) -> str:
    """
    Make the string "safe" by replacing all non-alphanumeric characters
    (with underscores by default).

    Args:
        string: The string which needs to be changed into a "safe" string.
        replacement_character: The character to replace all "unsafe" characters with.
        allowed_symbols: All characters given here will be ignored (kept and not replaced) in the string.

    Returns: A new string with "unsafe" characters replaced.

    """
    safe_characters = ascii_letters + digits + "".join(allowed_symbols)
    return "".join(character if character in safe_characters else replacement_character for character in string)


def md5_bytes(value: bytes | str) -> bytes:
    """
    Calculate the md5 hash of the input represented as a hexadecimal number.

    Args:
        value:
            The value to calculate the md5 sum of. If a string is given, it
            is encoded to bytes using UTF-8 encoding.
    """
    if isinstance(value, str):
        value = value.encode("utf-8")
    return hashlib.md5(value).digest()


def md5_hex(value: bytes | str, short: bool | int = False) -> str:
    """
    Calculate the md5 hash of the input represented as a hexadecimal number.

    Args:
        value:
            The value to calculate the md5 sum of. If a string is given, it
            is encoded to bytes using UTF-8 encoding.
        short:
            If an int is given, the result is truncated to this many characters.
            If True is given, it is equivalent to 7, which is the length of short
            hex IDs in Git.
            If False is given, the full length return is returned.

    Returns: A string containing the hexadecimal representation of the md5 sum value.
    """
    if short is False:
        length = None
    elif short is True:
        length = 7
    else:
        length = short
    return md5_bytes(value).hex()[:length]


def md5_int(value: bytes | str) -> int:
    """
    Calculate the md5 hash of the input as an int.

    Args:
        value:
            The value to calculate the md5 sum of. If a string is given, it
            is encoded to bytes using UTF-8 encoding.
    """
    return int.from_bytes(md5_bytes(value), "big")


def random_integer_string(length: int) -> str:
    """
    Return a string containing `length` digits. The string will not start with a zero.
    """
    if length < 0:
        raise ValueError("Call to random_integer_string with negative length.")
    if length == 0:
        return ""
    return str(random.randrange(pow(10, length - 1), pow(10, length)))


def readable_timestamp(
    time: typing.Optional[datetime.datetime] = None,
    unique: bool = False,
    decimals: int = 0,
) -> str:
    """
    Create a timestamp (numerical date and time string) in an easy-to-read format
    year-month-day hour:minute:second .

    Args:
        time: The datetime to format. By default, the current UTC time.
        unique: If True, an 8 digit random number is added to the end.
        decimals: How many decimal places of a second should be shown.

    Returns: A string in the format described.
    """
    return _timestamp("%Y-%m-%d %H:%M:%S", ".%f", " ", time, unique, decimals)


def dense_timestamp(
    time: typing.Optional[datetime.datetime] = None,
    unique: bool = False,
    decimals: int = 0,
) -> str:
    """
    Create a timestamp (numerical date and time string) in a compact format
    consisting of only numbers.

    Args:
        time: The datetime to format. By default, the current UTC time.
        unique: If True, an 8 digit random number is added to the end.
        decimals: How many decimal places of a second should be shown.

    Returns: A string in the format described.
    """

    return _timestamp("%Y%m%d%H%M%S", "%f", "", time, unique, decimals)


def safe_timestamp(
    time: typing.Optional[datetime.datetime] = None,
    unique: bool = False,
    decimals: int = 0,
    double_separator=False,
) -> str:
    """
    Create a timestamp (numerical date and time string) consisting of only numbers
    and underscores that is quite easy to read but safe for most computing uses.

    Args:
        time: The datetime to format. By default, the current UTC time.
        unique: If True, an 8 digit random number is added to the end.
        decimals: How many decimal places of a second should be shown.
        double_separator:
            If True, the date, time, and random number (if present) will be
            separated by double underscores (__). If False then a single underscore
            is used.

    Returns: A string in the format described.
    """
    if double_separator:
        separator = "__"
    else:
        separator = "_"
    return _timestamp(f"%Y_%m_%d{separator}%H_%M_%S", "_%f", separator, time, unique, decimals)


def _timestamp(
    time_format: str,
    decimals_format: str,
    separator: str,
    time: typing.Optional[typing.Any] = None,
    unique: bool = False,
    decimals: int = 0,
):
    """
    Create a timestamp (numerical date and time string).

    Args:
        time_format: The format of the datetime, as a strftime string.
        decimals_format:
            The format of the second decimals, including leading separator,
            as a strftime string.
        separator:
            The separator between the timestamp and timezone or unique,
            random number, if they are added.
        time: The datetime to format. By default, the current UTC time.
        unique: If True, an 8 digit random number is added to the end.
        decimals: How many decimal places of a second should be shown.

    Returns: A string in the format described.
    """
    if time is None:
        time = datetime.datetime.now(datetime.timezone.utc)
    result = time.strftime(time_format)
    if decimals < 0 or decimals > 6:
        raise ValueError("decimals must be an integer from 0 to 6.")
    # If 0 skip completely, to avoid leaving the separator.
    if decimals != 0:
        result += time.strftime(decimals_format)
        end_offset = decimals - 6
        if end_offset != 0:  # Python discontinuous slice behaviour
            result = result[:end_offset]
    if unique:
        result += separator + random_integer_string(8)
    return result
