from bank import value

def test_hello():
    assert value('hello')==0

def test_hi():
    assert value('hi')==20

def test_Hey():
    assert value('Hey')==20

def test_greeting():
    assert value('greeting')==100