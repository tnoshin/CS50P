from PIL import Image, ImageOps
import sys

if len(sys.argv)!=3:
    sys.exit('Error')
af = ('.jpg','.jpeg','.png')
if not sys.argv[1].lower().endswith(af) or not sys.argv[2].lower().endswith(af):
    sys.exit('Error')
if sys.argv[1].lower().split('.')[-1] != sys.argv[2].lower().split('.')[-1]:
    sys.exit('Error')

try:
    img = Image.open(sys.argv[1])
    shirt=Image.open('shirt.png')

    img= ImageOps.fit(img, shirt.size)
    img.paste(shirt, mask=shirt)
    img.save(sys.argv[2])

except FileNotFoundError:
    sys.exit('Error')

