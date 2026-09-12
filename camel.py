def main():
    x = input('camelCase:')
    print(convert(x))

def convert(x):
    snake =''
    for c in x:
            if c.isupper():
                snake += '_' + c.lower()
            else:
                snake += c
    return snake
main()

'''userinput = input('camelCase: ')


camel = ''
for c in userinput:
    if c.isupper():
        camel=  camel + '_' + c.lower()
    elif c.islower():
        camel = camel +c
    else:
        pass

print('snake_case: ',camel)
'''