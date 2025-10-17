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

# Input from user
amount = float(input("Enter initial amount: "))
increment = float(input("Enter the increment amount: "))
percentages_input = input("Enter the list of percentages (comma-separated): ")
percentages = list(map(float, percentages_input.split(',')))

# Initialize variables
previous = amount
total_invested = 0
total_net_profit = 0

print()

# Loop through each month and apply the corresponding percentage increase
for month, percent in enumerate(percentages, start=1):
    true_percent = 1 + (percent / 100)
    
    # Calculate the result after percentage increase
    result = previous * true_percent
    profit = result - previous
    
    # Add increment after each percentage (except the last one)
    if month < len(percentages):  # No increment after last month
        result += increment
        total_invested += increment
    
    # Calculate the net profit
    net_profit = result - amount - total_invested

    # Print details for the current month
    print(f"Iteration {month}:")
    print(f"  Percentage: {percent}%")
    print(f"  Current Amount: {format_in_indian_style(result)}")
    print(f"  Profit this time: {format_in_indian_style(profit)}")
    print(f"  Total Invested till now: {format_in_indian_style(total_invested)}")
    print(f"  Net Profit till now: {format_in_indian_style(net_profit)}")
    print()
    
    previous = result  # Update previous for the next time
