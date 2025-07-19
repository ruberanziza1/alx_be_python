
# Prompt the user to enter a positive integer for the pattern size
while True:
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer.")
        else:
            break # Exit the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter an integer number.")

# Initialize a counter for the while loop (for rows)
row_count = 0

# Use a while loop to iterate through each row of the pattern
while row_count < size:
    # Use a for loop to print asterisks for the current row
    # The range(size) function generates numbers from 0 up to (but not including) size,
    # which means it iterates 'size' times.
    for _ in range(size):
        # Print an asterisk without moving to a new line
        print("*", end="")
    
    # After printing all asterisks for the current row, print a newline character
    # to move to the next row
    print()
    
    # Increment the row counter
    row_count += 1

