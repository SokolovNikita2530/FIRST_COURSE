def is_valid_car_number(number):
    try:
        if not number:
            raise ValueError("Строка пуста.")
        if re.fullmatch(r'[A-Za-z]{2}\d{3}[A-Za-z]', number):
            return True
        else:
            raise ValueError("Номер не соответствует формату.")
    except ValueError as e:
        print(f"Ошибка: {e}")
        return False

def main():
    print("Введите строку для проверки:")
    number = input().strip()
    if is_valid_car_number(number):
        print(f"'{number}' может быть номером автомобиля.")
    else:
        print(f"'{number}' не является номером автомобиля.")

if __name__ == "__main__":
    main()

