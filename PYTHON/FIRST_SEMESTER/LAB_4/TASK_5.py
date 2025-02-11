def gcd(a, b):
    """Рекурсивно вычисляет наибольший общий делитель (НОД)."""
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    """Вычисляет наименьшее общее кратное (НОК) через НОД."""
    return abs(a * b) // gcd(a, b)

def main():
    try:
        num1 = int(input("Введите первое натуральное число: "))
        num2 = int(input("Введите второе натуральное число: "))
        if num1 <= 0 or num2 <= 0:
            raise ValueError("Числа должны быть натуральными.")
        result = lcm(num1, num2)
        print(f"Наименьшее общее кратное чисел {num1} и {num2}: {result}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
