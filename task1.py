# Task 1: Basic Mathematical Operations

# Take two numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

# Display results
print("\nResults:")
print(f"Addition:  {addition}")
print(f"Subtraction:  {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
