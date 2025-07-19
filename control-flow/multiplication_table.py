# Prompt the user to enter a number
# The input() function reads a string, so we convert it to an integer using int()
try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter an integer number.")
    # Exit the script if the input is not a valid integer
    exit()

# Generate and print the multiplication table using a for loop
# The range(1, 11) function generates numbers from 1 up to (but not including) 11,
# which means it generates numbers from 1 to 10.
print(f"\nMultiplication Table for {number}:\n")
for i in range(1, 11):
    # Calculate the product of the user's number and the current iterator (i)
    product = number * i
    # Print each line of the multiplication table in the specified format
    print(f"{number} * {i} = {product}")


