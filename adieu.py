import inflect
def main():
    name = []
    p=inflect.engine()
    while True:
        try:
            userinput = input('Name: ')
            name.append(userinput)
        except EOFError:
            print()
            break
    print('Adieu, adieu, to' , p.join(name))

main()
