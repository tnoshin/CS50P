import sys
count = 0
if len(sys.argv) !=2:
    sys.exit('Error')
if not sys.argv[1].endswith('.py'):
    sys.exit('Error')

try:
    with open(sys.argv[1]) as file:
        for line in file:
            if line.strip()=='':
                pass
            elif line.strip().startswith('#'):
                pass
            else:
                count +=1
except FileNotFoundError:
    sys.exit('Error')

print(count)


