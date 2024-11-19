from datetime import datetime

def calculate_train_travel_time():
    try:
        departure = input("Введите дату и время отправления (ГГГГ-ММ-ДД ЧЧ:ММ): ")
        arrival = input("Введите дату и время прибытия (ГГГГ-ММ-ДД ЧЧ:ММ): ")
        departure_time = datetime.strptime(departure, "%Y-%m-%d %H:%M")
        arrival_time = datetime.strptime(arrival, "%Y-%m-%d %H:%M")
        if arrival_time < departure_time:
            raise ValueError("Время прибытия не может быть раньше времени отправления.")
        travel_time = arrival_time - departure_time
        print(f"Время в пути: {travel_time}")
    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

if __name__ == "__main__":
    calculate_train_travel_time()
