def dot_product(vector1, vector2):
    try:
        if len(vector1) != len(vector2):
            raise ValueError("Размерности векторов не совпадают.")
        return sum(x * y for x, y in zip(vector1, vector2))
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

def main():
    try:
        print("Введите первый вектор через пробел:")
        vector1 = list(map(float, input().split()))
        print("Введите второй вектор через пробел:")
        vector2 = list(map(float, input().split()))
        result = dot_product(vector1, vector2)
        if result is not None:
            print(f"Скалярное произведение: {result}")
    except Exception as e:
        print(f"Ошибка ввода данных: {e}")

if __name__ == "__main__":
    main()

