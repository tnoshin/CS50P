def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('valid')
    else:
        print('invalid')

def is_valid(plate):
    if not 2 <= len(plate) <= 6:
        return False
    if not plate[0:2].isalpha():
        return False
    for c in plate:
        if not c.isalnum():
            return False
    number = False
    for c in plate:
        if c.isdigit():
            if not number and c=='0':
                return False
            number = True 
        elif number:
            return False
    return True
main()
    

            

