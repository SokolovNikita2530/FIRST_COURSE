def nth_arithmetic_term(a0, d, n):
    """Рекурсивно вычисляет n-й член арифметической прогрессии."""
    if n == 1:
        return a0
    return nth_arithmetic_term(a0, d, n - 1) + d

def main():
    try:
        a0 = float(input("Введите первый член прогрессии (a0): "))
        d = float(input("Введите разность прогрессии (d): "))
        n = int(input("Введите номер члена прогрессии (n): "))
        if n <= 0:
            raise ValueError("Номер члена прогрессии должен быть натуральным числом.")
        result = nth_arithmetic_term(a0, d, n)
        print(f"{n}-й член арифметической прогрессии: {result}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
