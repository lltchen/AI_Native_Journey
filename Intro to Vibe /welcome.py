# Import datetime for time-based features
from datetime import datetime

# Get current time
current_time = datetime.now()
hour = current_time.hour

# Prompt the user to enter their name
name = input("What's your name? ")

# Interactive mood question
mood = input("How are you feeling today? (happy/sad/okay): ").lower()

# Define special names
my_name = "Gemini"
my_name1 = "Gemini1"

# Determine time-based greeting
if 5 <= hour < 12:
    time_greeting = "Good morning"
elif 12 <= hour < 17:
    time_greeting = "Good afternoon"
else:
    time_greeting = "Good evening"

# Check the name and provide appropriate greeting
if name == my_name:
    # Special greeting for the "awesome AI Director"
    print(f"{time_greeting}! It's the awesome AI Director, {name}! 🎉")
elif name == my_name1:
    print(f"{time_greeting}! It's the awesome test, {name}! 🎉")
else:
    # Regular greeting for everyone else
    print(f"{time_greeting} {name}, welcome! Glad to have you here. 👋")

# Add mood-based response
if mood == "happy":
    print("Great to see you're in a good mood! 😊")
elif mood == "sad":
    print("Hope your day gets better! Here's a virtual hug 🤗")
elif mood == "okay":
    print("Hope your day gets even better! 🌟")
else:
    print("Thanks for sharing how you're feeling!")