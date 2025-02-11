import re

def is_valid_filename(filename):
    try:
        if not filename:
            raise ValueError("Строка пуста.")
        if not re.match(r'^[^<>/\\|?*]+$', filename):
            raise ValueError("Файл содержит недопустимые символы.")
        if not re.search(r'\.(txt|doc|docx|odt|rtf)$', filename, re.IGNORECASE):
            raise ValueError("Файл имеет недопустимое расширение.")
        return True
    except ValueError as e:
        print(f"Ошибка: {e}")
        return False

def main():
    print("Введите строки (пустая строка для завершения):")
    while True:
        line = input().strip()
        if not line:
            break
        if is_valid_filename(line):
            print(f"'{line}' может быть именем файла.")
        else:
            print(f"'{line}' не является именем файла.")

if __name__ == "__main__":
    main()

