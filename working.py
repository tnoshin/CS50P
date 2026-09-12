import re
import sys

def main():
    s = input("Hours: ")
    print(convert(s))



def convert(s):
    matches = re.search(r'^(\d+)(?::(\d{2}))? (AM|PM) to (\d+)(?::(\d{2}))? (AM|PM)$', s)
    if not matches:
        raise ValueError

    start_hour= matches.group(1)
    start_minute= matches.group(2) or '00'
    AM_orPM= matches.group(3)
    end_hour= matches.group(4)
    end_minute= matches.group(5) or '00'
    AMor_PM= matches.group(6)

    start_hour = int(matches.group(1))
    if AM_orPM=='AM':
        if start_hour == 12:
            start_hour=0
    elif AM_orPM=='PM':
        if start_hour != 12:
            start_hour+=12

    end_hour = int(matches.group(4))
    if AMor_PM=='AM':
        if end_hour == 12:
            end_hour=0
    elif AMor_PM=='PM':
        if end_hour != 12:
            end_hour+=12

    if int(start_minute) >=60:
        raise ValueError
    if int(end_minute) >=60:
        raise ValueError



    return f'{start_hour:02d}:{start_minute} to {end_hour:02d}:{end_minute}'


if __name__ == "__main__":
    main()
'''or'''
'''
import re

def main():
    s = input("Hours: ")
    print(convert(s))

def convert(s):
    matches = re.search(r'^(\d+)(?::(\d{2}))? (AM|PM) to (\d+)(?::(\d{2}))? (AM|PM)$', s)
    if not matches:
        raise ValueError
    st_hour= matches.group(1)
    st_minute= matches.group(2) or '00'
    ed_hour= matches.group(4)
    ed_minute= matches.group(5) or '00'
    st_time= matches.group(3)
    ed_time= matches.group(6)

    st_hour = int(st_hour)
    ed_hour = int(ed_hour)

    if int(st_minute)>=60:
        raise ValueError
    if int(ed_minute)>=60:
        raise ValueError


    start= time_change(st_time,st_minute, st_hour)
    end= time_change(ed_time,ed_minute, ed_hour)

    return f'{start} to {end}'

def time_change(time, minute, hour):
    if time=='AM':
        if hour ==12:
            hour =0
    elif time=='PM':
        if hour !=12:
            hour +=12

    return f'{hour:02d}:{minute}'
if __name__=='__main__':
    main()

'''