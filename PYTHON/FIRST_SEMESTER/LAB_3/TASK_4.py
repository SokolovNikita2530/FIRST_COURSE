from datetime import datetime, timedelta

def calculate_special_birthdays():
    try:
        birthday = input("Введите вашу дату рождения (ГГГГ-ММ-ДД): ")
        birth_date = datetime.strptime(birthday, "%Y-%m-%d")
        date_10000_days = birth_date + timedelta(days=10000)
        date_1000000_minutes = birth_date + timedelta(minutes=1000000)
        date_1000000000_seconds = birth_date + timedelta(seconds=1000000000)
        print(f"Дата, когда исполнится 10 000 дней: {date_10000_days}")
        print(f"Дата, когда исполнится 1 000 000 минут: {date_1000000_minutes}")
        print(f"Дата, когда исполнится 1 000 000 000 секунд: {date_1000000000_seconds}")
    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

if __name__ == "__main__":
    calculate_special_birthdays()
