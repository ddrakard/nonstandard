import nonstandard as ns


def test_empty_bytes():
    assert ns.md5_int(b"") == 281949768489412648962353822266799178366


def test_basic_bytes():
    assert ns.md5_int(b"a948hgd") == 131248504013170909277680080980298930782


def test_empty_string():
    assert ns.md5_int("") == 281949768489412648962353822266799178366


def test_basic_string():
    assert ns.md5_int("a948hgd") == 131248504013170909277680080980298930782
