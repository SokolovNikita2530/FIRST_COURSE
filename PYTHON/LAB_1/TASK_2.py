# Get the two numbers from the user
while True:
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Swap the values using a temporary variable
temp = a
a = b
b = temp

print(f"a = {a}, b = {b}")