def main():
    x = input('File name:').lower().strip()
    y(x)

def y(x):
    if x.endswith('.gif'):
        print('image/gif')
    elif x.endswith(('.jpg','.jpeg')):
        print('image/jpeg')
    elif x.endswith('.pdf'):
        print('application/pdf')
    elif x.endswith('.png'):
        print('image/png')
    elif x.endswith('.txt'):
        print('text/plain')
    elif x.endswith('.zip'):
        print('application/zip')
    else:
        print('application/octet-stream')
main()
