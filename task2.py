# Task 2: Personalized Greeting

# Take user's first and last name
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

# Concatenate and greet
full_name = f"{first_name} {last_name}"
print(f"\nHello, {full_name}! Welcome to the Python world!")
