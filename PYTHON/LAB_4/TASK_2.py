def sum_geometric_progression(a0, r, n):
    """Рекурсивно вычисляет сумму первых n членов геометрической прогрессии."""
    if n == 1:
        return a0
    return sum_geometric_progression(a0, r, n - 1) + nth_geometric_term(a0, r, n)

def nth_geometric_term(a0, r, n):
    """Рекурсивно вычисляет n-й член геометрической прогрессии."""
    if n == 1:
        return a0
    return nth_geometric_term(a0, r, n - 1) * r

def main():
    try:
        a0 = float(input("Введите первый член прогрессии (a0): "))
        r = float(input("Введите знаменатель прогрессии (r): "))
        n = int(input("Введите количество членов прогрессии (n): "))
        if n <= 0:
            raise ValueError("Количество членов должно быть натуральным числом.")
        result = sum_geometric_progression(a0, r, n)
        print(f"Сумма первых {n} членов геометрической прогрессии: {result}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
