# daily_reminder.py

# Prompt user for input
task = input("Enter your task for today: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Process the task using match-case based on priority
match priority:
    case "high":
        message = f"🔴 High Priority Task: {task}."
    case "medium":
        message = f"🟠 Medium Priority Task: {task}."
    case "low":
        message = f"🟢 Low Priority Task: {task}."
    case _:
        message = f"⚪ Unrecognized priority for task: {task}."

# Modify message if the task is time-sensitive
if time_bound == "yes":
    message += " This task requires immediate attention today!"

# Print customized reminder
print("\nReminder:")
print(message)

