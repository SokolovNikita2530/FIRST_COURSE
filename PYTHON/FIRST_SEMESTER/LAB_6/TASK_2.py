def format_string(s):
    try:
        if not s.strip():
            raise ValueError("Строка пуста.")
        # Удаление лишних пробелов и табуляций
        s = s.strip()
        # Приведение строки к формату
        s = s[0].upper() + s[1:].lower()
        if not s.endswith('.'):
            s += '.'
        return s
    except ValueError as e:
        print(f"Ошибка: {e}")
        return None

def main():
    print("Введите строку:")
    line = input()
    result = format_string(line)
    if result:
        print(f"Результат: {result}")

if __name__ == "__main__":
    main()

