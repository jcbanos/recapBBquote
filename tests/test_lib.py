from bbquote.lib import get_quote

def test_get_quote():
    quote = get_quote()
    assert len(quote) != 0 