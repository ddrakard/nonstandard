import nonstandard as ns


def test_already_safe():
    assert ns.identifierise("bhae832ad") == "bhae832ad"


def test_whitespace():
    assert ns.identifierise("uer eiw\nwa") == "uer_eiw_wa"


def test_underscore():
    assert ns.identifierise("hew_38") == "hew_38"


def test_empty():
    assert ns.identifierise("") == ""


def test_all_unsafe():
    assert ns.identifierise("*£ !") == "____"


def test_replacement_character():
    assert ns.identifierise("Ca's, ; to94", "*") == "Ca*s****to94"


def test_allowed_symbols():
    assert ns.identifierise("barl per_", ".", " .") == "barl per."
