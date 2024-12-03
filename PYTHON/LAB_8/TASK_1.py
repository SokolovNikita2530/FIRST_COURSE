def count_unique_characters(text):
    if not isinstance(text, str):
        raise ValueError("Ввод должен быть строкой.")
    unique_characters = set(text)
    return len(unique_characters)

def main():
    try:
        user_input = input("Введите строку текста: ")
        print(f"Количество уникальных символов: {count_unique_characters(user_input)}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()