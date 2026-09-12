from twttr import shorten
def test_lowercase():
    assert shorten('twitter')=='twttr'
def test_uppercase():
    assert shorten('HELLO')=='HLL'
def test_digit():
    assert shorten('cs50')=='cs50'
def test_mixed():
    assert shorten('Hello, World')=='Hll, Wrld'
#download pytest beforehand