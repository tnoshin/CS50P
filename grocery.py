def main():
    box ={}

    while True:
        try:
            cake = input()
        except EOFError:
            print()
            break

        if cake in box:
            box[cake] += 1
        else:
            box[cake] = 1

        for cake in sorted(box):
            print(box[cake], cake.upper())

main()



'''userinput = input('who?')

students = ['hermione','harry','ron']

if userinput in students:
    for i in range():
        print(i+1, students[i])'''