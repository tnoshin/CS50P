def main():
    line = input('Input: ')
    if is_valid(line):
        print('Valid')
    else:
        print('Invalid')

def is_valid(line):

    popcorn = False
    for c in line:
        if c.isdigit():
            if not popcorn and c=='0':
                return False
            popcorn = True
        elif popcorn:
            return False
    return True

main()