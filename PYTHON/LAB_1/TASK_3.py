import math 

# Get the sides of the triangle from the user
while True:
    try:
        a = int(input("Enter the first side: "))
        b = int(input("Enter the second side: "))
        c = int(input("Enter the third side: "))
        if a <= 0 or b <= 0 or c <= 0:
            print("Sides must be positive numbers. Try again!")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Check if the triangle is valid
if a + b > c and a + c > b and b + c > a:
    # Calculate the angles
    cos_A = (b**2 + c**2 - a**2) / (2 * b * c)
    cos_B = (a**2 + c**2 - b**2) / (2 * a * c)
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
    A = math.acos(cos_A)
    B = math.acos(cos_B)
    C = math.acos(cos_C)

    # Determine the type of triangle
    if A < math.pi / 2 and B < math.pi / 2 and C < math.pi / 2:
        print("The triangle is acute.")
    elif A == math.pi / 2 or B == math.pi / 2 or C == math.pi / 2:
        print("The triangle is right-angled.")
    else:
        print("The triangle is obtuse.")
else:
    print("The triangle is not valid.")