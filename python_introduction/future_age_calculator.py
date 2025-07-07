# This script calculates a user's future age based on their current age input.

# Prompt the user to input their current age
# The input() function reads a line from input, converts it to a string,
# and returns that string.
# We then convert the string to an integer using int() because we need to
# perform arithmetic operations on the age.
current_age = int(input("How old are you? "))

# Calculate the age in the year 2050.
# Assuming the current year is 2023, the difference to 2050 is 27 years.
years_to_add = 2050 - 2023
future_age = current_age + years_to_add

# Print the user's age in 2050 in the specified format
print(f"In 2050, you will be {future_age} years old.")

# To execute this script:
# 1. Save the code above into a file named 'future_age_calculator.py'.
# 2. Open your terminal or command prompt.
# 3. Navigate to the directory where you saved the file.
# 4. Run the script using the command: python3 future_age_calculator.py
# 5. When prompted, enter your current age and press Enter.

