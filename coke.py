def main():
    due = 50
    while due > 0 :
        print('Amount Due:', due)
        insert = int(input('Insert Coin:'))
        if insert == 5:
            due -= insert
            print('Amount Due:', due)
        elif insert ==10:
            due -= insert
            print('Amount Due:', due)
        elif insert == 25:
            due -= insert
            print('Amount Due:', due)
        else:
            print('Amount Due:', due)
        if due <= 0:
            print('Change Owed:', -due)

main()
