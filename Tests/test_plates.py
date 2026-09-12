from plates import is_valid
def test_tooshort():
    assert is_valid("A") == False
def test_correct_len2():
    assert is_valid("AA") == True
def test_correct_len3():
    assert is_valid("AAA") == True
def test_correct_len4():
    assert is_valid("AA22") == True
def test_correct_len5():
    assert is_valid("AAA11") == True
def test_correct_len6():
    assert is_valid("AAAAAA") == True
def test_01stc():
    assert is_valid("AAAAA0") == False
def test_nmbr1st():
    assert is_valid("1AA") == False
def test_nmbrmid():
    assert is_valid("AA1A") == False
def test_01st():
    assert is_valid("0AA") == False
def test_01stalpha():
    assert is_valid("A1") == False
def test_punctuation():
    assert is_valid("AA,AAA") == False
def test_period():
    assert is_valid("AA.AA") == False