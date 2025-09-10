def format_in_indian_style(number):
    num_str = f"{number:.2f}"
    integer_part, decimal_part = num_str.split(".")

    integer_part_reversed = integer_part[::-1]
    integer_part_with_commas = ""
    for i in range(len(integer_part_reversed)):
        if i == 3 or (i > 3 and (i - 3) % 2 == 0):
            integer_part_with_commas += ","
        integer_part_with_commas += integer_part_reversed[i]

    integer_part_with_commas = integer_part_with_commas[::-1]
    return f"{integer_part_with_commas}.{decimal_part}"


amount = float(input("Enter initial amount: "))
percent = float(input("Enter the percentage: "))
months = int(input("Enter the number of months: "))
increment = float(input("Enter the monthly increment amount: "))

true_percent = 1 + (percent / 100)

previous = amount
print()

for month in range(1, months + 1):
    result = previous * true_percent
    profit = result - previous
    result += increment  # Add the monthly increment at the end
    
    # Calculate net profit after the increment for the current month
    total_invested = increment * month  # Only increments are considered as invested
    net_profit = result - amount - total_invested  # Subtract initial amount and increments

    # Print details after each month
    print(f"Month {month}:")
    print(f"  Current Amount: {format_in_indian_style(result)}")
    print(f"  Profit this month: {format_in_indian_style(profit)}")
    print(f"  Total Invested till now: {format_in_indian_style(total_invested)}")
    print(f"  Net Profit till now: {format_in_indian_style(net_profit)}")
    print()
    
    previous = result
