# This script calculates a user's monthly savings and projects their annual savings
# with a simple interest rate, based on user-provided income and expenses.

# --- User Input for Financial Details ---

# Prompt the user for their monthly income.
# The input() function reads the user's input as a string.
# int() is used to convert this string to an integer for calculations.
monthly_income = int(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses.
monthly_expenses = int(input("Enter your total monthly expenses: "))

# --- Calculate Monthly Savings ---

# Calculate the monthly savings by subtracting expenses from income.
monthly_savings = monthly_income - monthly_expenses

# --- Project Annual Savings ---

# Define the simple annual interest rate (5% as a decimal).
annual_interest_rate = 0.05

# Calculate the projected savings after one year.
# This includes the accumulated monthly savings over 12 months,
# plus the interest earned on that accumulated amount.
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

# --- Output Results ---

# Display the user's monthly savings.
print(f"Your monthly savings are ${monthly_savings}.")

# Display the projected annual savings after including interest.
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings}.")

# To execute this script:
# 1. Save the code above into a file named 'finance_calculator.py'.
# 2. Open your terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the script using the command: python3 finance_calculator.py
# 5. When prompted, enter your monthly income and expenses and press Enter after each.

