def main():
    x = input('Input:')
    
    result = ''
    for c in x:
        if c.lower() not in ('a','e','i','o','u'):
            result += c

    print('Output:', result)
main()
'''
userinput = input('Input: ')


twttr = ''
for c in userinput:
    if c not in ('a','e','i','o','u'):
        twttr += c

print('Output: ', twttr)

or

def main():
    word = input('Input:')
    result = shorten(word)
    print('Output: ', result)

def shorten(word):
    twttr = ''
    for c in word:
        if c.lower() not in ('a','e','i','o','u'):
            twttr = twttr + c
    return twttr

if __name__=='__main__':
    main()
'''