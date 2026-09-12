import re
import sys


def main():
    ip= input("IPv4 Address: ")
    print(validate(ip))


def validate(ip):
    if match := re.search(r'^(\d+)\.(\d+)\.(\d+)\.(\d+)$', ip):
        a,b,c,d = match.groups()
        for x in [a,b,c,d]:
            if not (0 <= int(x) <= 255):
                return False
            if len(x)> 1 and x[0]=='0':
                return False
        return True
    return False


if __name__ == "__main__":
    main()

or
'''
import sys
import re

def main():
    ip = input('IPv4 Address: ')
    print(validate(ip))

def validate(ip):
    if match := re.search(r'^(\d+)\.(\d+)\.(\d+)\.(\d+)$', ip):
        a,b,c,d = match.groups()
        grouped = [a,b,c,d]

        for x in grouped:
            if not (0 <= int(x) <= 255) or len(x)>1 and x[0]=='0':
                return False
        return True
    return False

if __name__=='__main__':
    main()
'''