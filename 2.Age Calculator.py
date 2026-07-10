from datetime import datetime

# Automatically get the current year (2026)
current_year = datetime.now().year

# Define the user's birth year (example: 2000)
birth_year = 2000

# Calculate the age using the subtraction operator (-)
age = current_year - birth_year

# Display the result
print(f"Current Year: {current_year}")
print(f"Birth Year: {birth_year}")
print(f"The user's age is: {age} years old.")