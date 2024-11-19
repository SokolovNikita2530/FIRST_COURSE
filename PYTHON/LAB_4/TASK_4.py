def decimal_to_binary(n):
    """Рекурсивно преобразует десятичное число в двоичное представление."""
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)

def main():
    try:
        number = int(input("Введите десятичное число: "))
        if number < 0:
            raise ValueError("Число должно быть неотрицательным.")
        result = decimal_to_binary(number)
        print(f"Двоичное представление числа {number}: {result}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
