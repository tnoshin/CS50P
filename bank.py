def main():
    x = input('Greeting: ').lower().strip()
    y(x)

def y(x):
    if x[0:5]==('hello') : #or x.startswith('hello')
        print('$0')
    elif x[0] == 'h':
        print('$20')
    else:
        print('$100')

main()

'''
def main():
    greeting = input('Greeting: ').lower().strip()
    print(f'${value(greeting)}')

def value(greeting):
    greeting = greeting.lower()
    if greeting[0:5]==('hello') : #or x.startswith('hello')
        return '0'
    elif greeting[0] == 'h':
        return '20'
    else:
        return '100'

if __name__=='__main__':
    main()
'''