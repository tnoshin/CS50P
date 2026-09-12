def main():
    time = input('What time is it? ')
    result = convert(time)


    if 7.00 <= result <= 8.00:
        print('breakfast time')
    elif 12.00 <= result <= 13.00:
        print('lunch time')
    elif 18.00 <= result <= 19.00:
        print('dinner time')
    else:
        pass

def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + (float(int(minutes)/60))



if __name__ == "__main__":
    main()


#additionsatthebottom

#my previous way of solving
'''def main():
    time = input('What time is it? ')
    hours, minutes = time.split(":")
    convert = float(hours) + (float(int(minutes)/60))

    if 7.00 <= convert < 8.00:
        print('breakfast time')
    elif 12.00 <= convert < 13.00:
        print('lunch time')
    elif 18.00 <= convert < 19.00:
        print('dinner time')
    else:
        pass


if __name__ == "__main__":
    main()'''






























'''
def main():
    time = int(input('What time is it?').replace(':',''))
    if 700 <= time <800:
        print('breakfast time')
    elif 1200 <= time < 1300:
        print('lunch time')
    elif 1800 <= time < 1900:
        print('dinner time')
    else:
        pass

main()
'''