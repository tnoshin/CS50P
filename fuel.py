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