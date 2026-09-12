import sys
import re
from datetime import date
import inflect

def main():
    userinput = input('Date of Birth: ')
    if results(userinput):
        print(results(userinput))
    else:
        sys.exit('Invalid')

def results(userinput):
    matches= re.search(r'^(\d{4})-(\d{2})-(\d{2})$', userinput)
    if not matches:
        return False
    year = matches.group(1)
    month = matches.group(2)
    day = matches.group(3)

    year=int(year)
    month=int(month)
    day=int(day)

    try:
        birthday= date(year,month,day)
    except ValueError:
        return False


    birthday = date(year,month,day)
    today = date.today()
    minutes = (today - birthday).days *1440


    p=inflect.engine()
    result= p.number_to_words(minutes, andword ='') + ' minutes'
    return result.capitalize()


if __name__=='__main__':
    main()


'''
'''or '''


import sys
import inflect
import re
from datetime import date

def main():
    userinput = input('Birth of Date: ')
    result = output(userinput)
    if result:
        print(result)
    else:
        sys.exit('Invalid')


def output(userinput):
    matches = re.search(r'^(\d{4})-(\d{2})-(\d{2})$',userinput)
    if not matches:
        return False
    year, month, day = matches.groups()
    year= int(year)
    month= int(month)
    day = int(day)

    try:
        birthday=date(year,month,day)
    except ValueError:
        return False
    today = date.today()
    minutes= (today-birthday).days *1440

    p= inflect.engine()
    final = p.number_to_words(minutes,  andword="") + ' minutes'
    return final.capitalize()

if __name__=='__main__':
    main()
'''




