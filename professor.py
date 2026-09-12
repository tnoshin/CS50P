import random
def main():
    score = 0
    level = get_level()
    for pikachu in range(10):
        x=generate_integer(level)
        y=generate_integer(level)
        for togepi in range(3):
            z = int(input(f'{x}+{y}='))
            try:
                if z== x+y:
                    score+=1
                    break
                else:
                    print('EEE')
            except ValueError: 
                print('EEE') 
        else:
            print(f'{x}+{y}={x+y}')
    print(score)


def get_level():
    while True:
        try:
            level=int(input('Level: '))
            if 0<level<4:
                return level
        except ValueError:
            pass

def generate_integer(level):
    if level==1:
        return random.randint(0,9)
    elif level==2:
        return random.randint(10,99)
    elif level==3:
        return random.randint(100,999)
    else:
        raise ValueError

main()