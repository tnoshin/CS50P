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




'''def main():
    while True:
        try:
            userinput = input('Fraction: ')
            x, y = userinput.split('/')
            x = int(x)
            y = int(y) 
            fraction = convert(fraction)
            percentage = gauge(percentage)

            if x > y or y <= 0 or x < 0:
                raise ValueError

            if percentage <= 1:
                print('E')
            elif percentage >= 99:
                print('F')
            else:
                print(f'{percentage}%')

            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    fraction= round((x / y))


def gauge(percentage):
    percentage= fraction*100


if __name__ == "__main__":
    main()
    
    
def main():
    while True:
        try:
            fraction = input('Fraction: ')
            result = convert(fraction)
            print (gauge(result))
            break
        except (ValueError, ZeroDivisionError):
            pass
def convert(fraction):
    x, y = fraction.split('/')
    x = int(x)
    y = int(y)
    if x > y or y == 0 or x < 0:
        raise ValueError
    result =  round((x / y) * 100)
    return result

def gauge(result):
    if result <= 1:
        return 'E'
    elif result >= 99:
        return 'F'
    else:
        return f'{result}%'

if __name__ == "__main__":
    main()
    
def main():
    while True:
        try:
            fraction = input('Fraction: ')
            result = convert(fraction)
            print (gauge(result))
            break
        except (ValueError, ZeroDivisionError):
            pass
def convert(fraction):
    x, y = fraction.split('/')
    x = int(x)
    y = int(y)
    if x > y or y == 0 or x < 0:
        raise ValueError
    result =  round((x / y) * 100)
    return result

def gauge(result):
    if result <= 1:
        return 'E'
    elif result >= 99:
        return 'F'
    else:
        return f'{result}%'

if __name__ == "__main__":
    main()
'''