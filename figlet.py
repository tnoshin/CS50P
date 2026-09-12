import pyfiglet
import sys
import random

if len(sys.argv)==1:
    x = input('Input:')
    font1 = random.choice(pyfiglet.FigletFont.getFonts())
    y= pyfiglet.figlet_format(x, font=font1)
    print('Output:',y)
elif len(sys.argv)==3 and sys.argv[1] in ['-f','--font']:
    font2 = sys.argv[2]
    if font2 not in pyfiglet.FigletFont.getFonts():
        sys.exit("Invalid argument")
    x = input('Input:')
    try:
        y= pyfiglet.figlet_format(x, font=font2)
        print('Output:',y)
    except pyfiglet.FontNotFound:
        sys.exit("Invalid argument")
else:
    sys.exit("Invalid argument")
