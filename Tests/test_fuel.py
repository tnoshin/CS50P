import pytest
from fuel import convert, gauge

def test_convert():
    assert convert('1/4') == 25
def test_con1():
    with pytest.raises (ValueError):
        convert('5/4')
def test_con2():
    with pytest.raises (ZeroDivisionError):
        convert('1/0')
def test_con3():
    with pytest.raises (ValueError):
        convert('-1/4')

def test_gauge1():
    assert gauge(0)=='E'
def test_gauge11():
    assert gauge(1)=='E'
def test_gauge2():
    assert gauge(100)=='F'
def test_gauge21():
    assert gauge(99)=='F'
def test_gauge3():
    assert gauge(50)=='50%'


