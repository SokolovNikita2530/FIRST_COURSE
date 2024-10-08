# Get the salary from the user
while True:
    try:
        N = float(input("Enter the salary: "))
        if N <= 0:
            print("Salary must be a positive number. Try again!")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Calculate the quarterly bonus and net salary
bonus = N * 2 / 3
tax = bonus * 0.13
net_salary = bonus - tax

print(f"Quarterly bonus: {bonus:.2f}")
print(f"Net salary: {net_salary:.2f}")