def format_in_indian_style(number):
    # Convert the number to a string
    num_str = f"{number:.2f}"
    integer_part, decimal_part = num_str.split(".")
    
    # Reverse the integer part and insert commas every 2 digits after the first 3
    integer_part_reversed = integer_part[::-1]
    integer_part_with_commas = ""
    for i in range(len(integer_part_reversed)):
        if i == 3 or (i > 3 and (i - 3) % 2 == 0):
            integer_part_with_commas += ","
        integer_part_with_commas += integer_part_reversed[i]
    
    # Reverse back the integer part
    integer_part_with_commas = integer_part_with_commas[::-1]
    
    # Join with the decimal part
    return f"{integer_part_with_commas}.{decimal_part}"

amount = float(input("amount: "))
percent = float(input("enter the percentage: "))
true_percent = 1 + (percent / 100)
months = int(input("enter the no. of months: "))

previous = amount
print()

for month in range(1, months + 1):
    result = previous * true_percent
    profit = result - previous
    print(f"Month {month}: {format_in_indian_style(result)}")
    print(f"Profit: {format_in_indian_style(profit)}")
    print()
    previous = result