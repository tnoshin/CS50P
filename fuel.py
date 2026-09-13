def main():
    while True:
        try:
            userinput = input('Fraction: ')
            x, y = userinput.split('/')
            x = int(x)
            y = int(y)
            result = round((x / y) * 100)

            if x > y or y <= 0 or x < 0:   
                raise ValueError

            if result <= 1:
                print('E')
            elif result >= 99:
                print('F')
            else:
                print(f'{result}%')

            break
        except (ValueError, ZeroDivisionError):
            pass

main()

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