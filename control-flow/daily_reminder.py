# Prompt the user for the task description
task = input("Enter your task: ")

# Prompt the user for the task's priority level
priority = input("Priority (high/medium/low): ").lower() # Convert to lowercase for easier matching

# Prompt the user if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower() # Convert to lowercase for easier matching

# Initialize the reminder message
reminder_message = ""

# Process the task based on priority using a match-case statement
match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task"
    case "medium":
        reminder_message = f"'{task}' is a medium priority task"
    case "low":
        reminder_message = f"'{task}' is a low priority task"
    case _: # Default case for invalid priority input
        reminder_message = f"'{task}' has an unrecognized priority"

# Modify the reminder if the task is time-bound using an if statement
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
elif time_bound == "no":
    # Add a specific message for non-time-bound low priority tasks
    if priority == "low":
        reminder_message += ". Consider completing it when you have free time."
    else:
        reminder_message += ". You can plan to complete this soon." # General message for non-time-bound
else:
    reminder_message += ". (Time-bound status not clearly specified)."

# Print the customized reminder
# Removed the leading newline from the string to match the expected format
print(f"Reminder: {reminder_message}")

# Optional: Add a celebratory message and a tweet link as requested
print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
print("🚀 Click here to tweet! 🚀")

