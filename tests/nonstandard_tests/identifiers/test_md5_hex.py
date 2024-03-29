import nonstandard as ns


def test_empty_bytes():
    assert ns.md5_hex(b"") == "d41d8cd98f00b204e9800998ecf8427e"


def test_basic_bytes():
    assert ns.md5_hex(b"a948hgd") == "62bd8adaf4ab394b10d56efab08b9a5e"


def test_short_bytes():
    assert ns.md5_hex(b"a948hgd", short=True) == "62bd8ad"


def test_first_bytes():
    assert ns.md5_hex(b"a948hgd", short=10) == "62bd8adaf4"


def test_empty_string():
    assert ns.md5_hex("") == "d41d8cd98f00b204e9800998ecf8427e"


def test_basic_string():
    assert ns.md5_hex("a948hgd") == "62bd8adaf4ab394b10d56efab08b9a5e"


def test_short_string():
    assert ns.md5_hex("a948hgd", short=True) == "62bd8ad"


def test_first_string():
    assert ns.md5_hex("a948hgd", short=10) == "62bd8adaf4"
