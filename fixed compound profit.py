def format_indian(number):
    """Formats a number with Indian comma separators (e.g., 1,00,000)"""
    s = str(int(number))  # Handle whole numbers
    if len(s) > 3:
        last_three = s[-3:]
        remaining = s[:-3]
        formatted = ""
        while len(remaining) > 0:
            if len(remaining) <= 2:  # Handle remaining 1 or 2 digits
                formatted = remaining + "," + formatted
                remaining = ""
            else:
                formatted = remaining[-2:] + "," + formatted
                remaining = remaining[:-2]
        formatted = formatted + last_three
    else:
        formatted = s
    return formatted

def investment_simulation():
    # Get user inputs
    initial_capital = float(input("Enter the initial capital (₹): "))
    monthly_return_percent = float(input("Enter the monthly return percentage (%): ")) / 100
    num_months = int(input("Enter the number of months to simulate: "))
    
    current_capital = initial_capital
    accumulated_profit = 0
    set_aside_amount = 0
    reinvestment_count = 0
    
    print("\nMonth-by-Month Breakdown:")
    print(f"{'Month':<10}{'Capital':<20}{'Profit':<20}{'Accumulated Profit':<25}{'Reinvested':<20}{'Set Aside':<20}")
    print("-" * 115)
    
    for month in range(1, num_months + 1):
        # Calculate profit for this month
        profit = current_capital * monthly_return_percent
        accumulated_profit += profit
        
        # Check if accumulated profit reaches current capital
        if accumulated_profit >= current_capital:
            # Reinvest current capital amount, set aside the rest
            reinvest_amount = current_capital
            additional_profit = accumulated_profit - current_capital
            current_capital += reinvest_amount
            set_aside_amount += additional_profit
            reinvestment_count += 1
            accumulated_profit = 0  # Reset profit counter
        else:
            reinvest_amount = 0
            additional_profit = 0
        
        # Print monthly details (formatted with Indian commas)
        print(f"{month:<10}₹{format_indian(current_capital):<20}₹{format_indian(profit):<20}₹{format_indian(accumulated_profit):<25}₹{format_indian(reinvest_amount):<20}₹{format_indian(additional_profit):<20}")
    
    # Final summary (formatted with Indian commas)
    print("\nFinal Results:")
    print(f"Initial Capital: ₹{format_indian(initial_capital)}")
    print(f"Monthly Return: {monthly_return_percent*100:.2f}%")
    print(f"Final Capital: ₹{format_indian(current_capital)}")
    print(f"Number of Reinvestments: {reinvestment_count}")
    print(f"Amount Set Aside: ₹{format_indian(set_aside_amount)}")
    print(f"Total Value (Capital + Set Aside): ₹{format_indian(current_capital + set_aside_amount)}")

# Run the simulation
investment_simulation()