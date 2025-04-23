def principle():
    amount = float(input("amount: "))
    return amount

def details():
    percent = float(input("enter the percentage: "))
    true_percent = 1 + (percent / 100)
    period = int(input("enter the no. of months: "))
    return true_percent, period

def compound(principal, true_percent, period):
    result = principal * (true_percent ** period)
    return result

def main():
    amount = principle()
    true_percent, period = details()
    final = compound(amount, true_percent, period)
    print(f"Final amount: {final}")

if __name__ == '__main__':
    main()