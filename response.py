import validators

userinput= input("what's your email?")

result = validators.email(userinput)

if result:
    print('Valid')
else:
    print('Invalid')


or:
import validators
ui = input("What's your name?")

if validators.email(ui):
    print("Valid")
else:
    print("Invalid")
