# match_case_calculator.py
# Simple Calculator with Match Case
# Objective: Learn to use Match Case statements for handling multiple operations

def main():
    """
    Main function that implements a simple calculator using Match Case statements.
    Prompts user for two numbers and an operation, then performs the calculation.
    """
    
    # Prompt for user input - two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Ask for the operation
    operation = input("Choose the operation (+, -, *, /): ").strip()
    
    # Perform calculation using Match Case statement
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}.")
        
        case "-":
            result = num1 - num2
            print(f"The result is {result}.")
        
        case "*":
            result = num1 * num2
            print(f"The result is {result}.")
        
        case "/":
            if num2 != 0:
                result = num1 / num2
                print(f"The result is {result}.")
            else:
                print("Cannot divide by zero.")
        
        case _:
            print("Invalid operation. Please choose +, -, *, or /.")

# Run the program when the script is executed directly
if __name__ == "__main__":
    main()
