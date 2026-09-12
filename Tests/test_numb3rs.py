import pytest
from numb3rs import validate

def test_t1():
    assert validate("201.3.6.28") == True
def test_t2():
    assert validate("275.3.6.28") == False
def test_t3():
    assert validate("2224.3.6.28") == False
def test_t4():
    assert validate("2222.344.6.28") == False
def test_t5():
    assert validate("222.344.6444.28") == False
def test_t6():
    assert validate("222.344.444.2888") == False
def test_t7():
    assert validate("222.3444.6.28") == False
def test_t8():
    assert validate("cat") == False
def test_t9():
    assert validate("222.cat.6.28") == False
def test_t10():
    assert validate("222.4.6cat.28") == False
def test_t11():
    assert validate("0.0.0.0") == True
def test_t12():
    assert validate("255.255.255.255") == True
