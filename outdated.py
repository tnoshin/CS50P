def main():
    months = {
        "January": 1, "February": 2, "March": 3,
        "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9,
        "October": 10, "November": 11, "December": 12
    }
    while True:
        try:
            userinput = input('Date:')
            if '/' in userinput:
                day, month, year = userinput.split('/')
                day = int(day)
                month= int(month)
                year = int(year)
            else:
                monthstr, day, year = userinput.split(' ')
                month = months[monthstr]
                day = day.rstrip(',')
                day = int(day)
                year = int(year)

            if day > 31 or day < 1  or month>12 or month<1:
                raise ValueError
            print(f'{year}-{month:02d}-{day:02d}')
            break

        except (ValueError, KeyError):
                pass

main()
