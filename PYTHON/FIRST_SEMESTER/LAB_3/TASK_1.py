import math

def calculate_trig_functions():
    try:
        angle = float(input("Введите угол в градусах: "))
        angle_rad = math.radians(angle)
        print(f"Синус: {math.sin(angle_rad):.5f}")
        print(f"Косинус: {math.cos(angle_rad):.5f}")
        print(f"Тангенс: {math.tan(angle_rad):.5f}")
    except ValueError:
        print("Ошибка: угол должен быть числом.")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

if __name__ == "__main__":
    calculate_trig_functions()

