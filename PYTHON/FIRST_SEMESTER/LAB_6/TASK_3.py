def remove_except_last(s1, s2):
    try:
        if not s2:
            raise ValueError("Вторая строка пуста.")
        parts = s1.split(s2)
        if len(parts) <= 1:
            return s1
        return s2.join(parts[:-1]) + s2 + parts[-1]
    except ValueError as e:
        print(f"Ошибка: {e}")
        return None

def main():
    print("Введите первую строку:")
    s1 = input()
    print("Введите вторую строку:")
    s2 = input()
    result = remove_except_last(s1, s2)
    if result:
        print(f"Результат: {result}")


if __name__ == "__main__":
    main()

