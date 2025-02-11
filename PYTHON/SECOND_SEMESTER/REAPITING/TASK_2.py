import math

def gcd(a, b):
    return math.gcd(a, b)

def print_coprime_table(N):
    try:
        N = int(input("Enter the number N: "))
        if N <= 0:
            raise ValueError("N must be a positive number.")
        for i in range(1, N+1):
            row = []
            for j in range(1, N+1):
                if gcd(i, j) == 1:
                    row.append("X")
                else:
                    row.append("O")
            print(" ".join(row))
    except ValueError as e:
        print(f"Error: {e}")

print_coprime_table(0)
