import re
import sys


def main():
    s=input("Text: ")
    print(count(s))


def count(s):
    match = re.findall(r'\bum\b', s, re.IGNORECASE)
    return len(match)



if __name__ == "__main__":
    main()

'''tests:
import pytest
from um import count

def test_convert1():
    assert count('um') == 1
def test_convert2():
    assert count('um?') == 1
def test_convert3():
    assert count('Um, thanks for the album.') == 1
def test_convert4():
    assert count('Um, thanks, um...') == 2

    '''