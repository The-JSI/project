def principle():
    amount = float(input("amount: "))
    return amount

def details():
    percent = float(input("enter the percentage: "))
    true_percent = 1 + (percent / 100)
    months = int(input("enter the no. of months: "))
    return true_percent, months

def compound(amount, true_percent, months):
    result = amount * (true_percent **  months)
    return result

def main():
    amount = principle()
    true_percent, months = details()
    final = compound(amount, true_percent, months)
    print(f"Final amount: {final}")

if __name__ == '__main__':
    main()