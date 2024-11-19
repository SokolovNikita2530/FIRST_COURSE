def nth_geometric_term(a0, r, n):
    """Рекурсивно вычисляет n-й член геометрической прогрессии."""
    if n == 1:
        return a0
    return nth_geometric_term(a0, r, n - 1) * r

def main():
    try:
        a0 = float(input("Введите первый член прогрессии (a0): "))
        r = float(input("Введите знаменатель прогрессии (r): "))
        n = int(input("Введите номер члена прогрессии (n): "))
        if n <= 0:
            raise ValueError("Номер члена прогрессии должен быть натуральным числом.")
        result = nth_geometric_term(a0, r, n)
        print(f"{n}-й член геометрической прогрессии: {result}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
