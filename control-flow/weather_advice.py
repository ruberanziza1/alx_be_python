# weather_advice.py
# Weather Recommendation Program
# Objective: Utilize conditional statements to guide program execution based on user input

def main():
    """
    Main function that handles weather input and provides clothing recommendations.
    Uses if, elif, and else statements to make decisions based on user input.
    """
    # Prompt user for weather input
    weather = input("What's the weather like today? (sunny/rainy/cold): ").lower().strip()
    
    # Provide clothing recommendations based on weather conditions
    if weather == "sunny":
        print("Wear a t-shirt and sunglasses.")
    elif weather == "rainy":
        print("Don't forget your umbrella and a raincoat.")
    elif weather == "cold":
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

# Run the program when the script is executed directly
if __name__ == "__main__":
    main()
