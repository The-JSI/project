def format_indian(number):
    """Formats a number with Indian comma separators (e.g., 1,00,000)"""
    num_str = str(int(round(number)))
    if len(num_str) > 3:
        last_three = num_str[-3:]
        remaining = num_str[:-3]
        formatted = ""
        while len(remaining) > 0:
            if len(remaining) == 2:
                formatted = remaining + "," + formatted
                remaining = ""
            elif len(remaining) == 1:
                formatted = remaining + "," + formatted
                remaining = ""
            else:
                formatted = remaining[-2:] + "," + formatted
                remaining = remaining[:-2]
        formatted = formatted + last_three
    else:
        formatted = num_str
    return formatted

def investment_simulation():
    initial_capital = float(input("Enter the initial capital (₹): "))
    monthly_return_percent = float(input("Enter the monthly return percentage (%): ")) / 100
    num_months = int(input("Enter the number of months to simulate: "))
    
    current_capital = initial_capital
    accumulated_profit = 0
    set_aside_amount = 0
    reinvestment_count = 0
    
    print("\nMonth-by-Month Breakdown:")
    headers = ["Month", "Capital", "Profit", "Accumulated Profit", "Reinvested", "Set Aside"]
    print(f"{headers[0]:<10}{headers[1]:<20}{headers[2]:<20}{headers[3]:<25}{headers[4]:<20}{headers[5]:<20}")
    print("-" * 115)
    
    for month in range(1, num_months + 1):
        profit = current_capital * monthly_return_percent
        accumulated_profit += profit
        
        if accumulated_profit >= current_capital:
            reinvest_amount = current_capital
            additional_profit = accumulated_profit - current_capital
            current_capital += reinvest_amount
            set_aside_amount += additional_profit
            reinvestment_count += 1
            accumulated_profit = 0
        else:
            reinvest_amount = 0
            additional_profit = 0
        
        print(f"{month:<10}₹{format_indian(current_capital):<20}₹{format_indian(profit):<20}₹{format_indian(accumulated_profit):<25}₹{format_indian(reinvest_amount):<20}₹{format_indian(additional_profit):<20}")
    
    # CORRECTED TOTAL VALUE CALCULATION
    total_value = current_capital + set_aside_amount + accumulated_profit
    
    print("\nFinal Results:")
    print(f"Initial Capital: ₹{format_indian(initial_capital)}")
    print(f"Monthly Return: {monthly_return_percent*100:.2f}%")
    print(f"Final Capital: ₹{format_indian(current_capital)}")
    print(f"Number of Reinvestments: {reinvestment_count}")
    print(f"Amount Set Aside: ₹{format_indian(set_aside_amount)}")
    print(f"Unallocated Profit: ₹{format_indian(accumulated_profit)}")
    print(f"Total Value: ₹{format_indian(total_value)}")

investment_simulation()