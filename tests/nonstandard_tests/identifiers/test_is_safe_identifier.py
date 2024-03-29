import nonstandard as ns


def test_already_safe():
    assert ns.is_safe_identifier("bhae832ad")


def test_whitespace():
    assert not ns.is_safe_identifier("uer eiw\nwa")


def test_underscore():
    assert ns.is_safe_identifier("hew_38")


def test_empty():
    assert not ns.is_safe_identifier("")


def test_all_unsafe():
    assert not ns.is_safe_identifier("*£ !")


def test_allowed_symbols():
    assert ns.is_safe_identifier("ca far", " -")


def test_no_allowed_symbols():
    assert not ns.is_safe_identifier("ire_23", "")
