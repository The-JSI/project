amount = float(input("amount: "))
percent = float(input("enter the percentage: "))
true_percent = 1 + (percent / 100)
months = int(input("enter the no. of months: "))

previous = amount
print()

for month in range(1, months + 1):
    result = previous * true_percent
    profit = result - previous
    print(f"Month {month}: {result:.2f}")
    print(f"Profit: {profit:.2f}")
    print()
    previous = result