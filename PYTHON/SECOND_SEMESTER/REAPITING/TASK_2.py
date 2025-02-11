def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def print_coprime_table(N):
    try:
        N = int(input("Enter the number N: "))
        if N <= 0:
            raise ValueError("N must be a positive number.")
        
        print("   ", end="")
        for i in range(1, N+1):
            print(f"{i:2}", end="")
        print()
        
        for i in range(1, N+1):
            print(f"{i:2} ", end="")
            for j in range(1, N+1):
                if gcd(i, j) == 1:
                    print(" X", end="")
                else:
                    print(" O", end="")
            print()

    except ValueError as e:
        print(f"Error: {e}")

print_coprime_table(0)
