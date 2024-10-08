import math

# Get the coordinates of the vector from the user
while True:
    try:
        x = float(input("Enter the x-coordinate: "))
        y = float(input("Enter the y-coordinate: "))
        z = float(input("Enter the z-coordinate: "))
        break
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Calculate the length of the vector
length = math.sqrt(x**2 + y**2 + z**2)

print(f"The length of the vector is {length:.2f}")