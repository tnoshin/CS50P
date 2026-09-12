def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars):
        dollar = dollars.strip('$')
        return float(dollar)


def percent_to_float(percent):
    p = percent.strip('%')
    y = float(p)
    return (y*0.01)


main()
