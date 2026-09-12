import pytest
from seasons import results

def test_convert1():
    assert results('2025-07-05') == 'Five hundred twenty-five thousand, six hundred minutes'
def test_convert2():
    assert results('2023-07-05') == 'One million, five hundred seventy-eight thousand, two hundred forty minutes'
