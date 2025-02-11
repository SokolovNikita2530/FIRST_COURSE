import math

def gcd_custom(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def calculate_gcd():
    try:
        num1 = int(input("Введите первое натуральное число: "))
        num2 = int(input("Введите второе натуральное число: "))
        if num1 <= 0 or num2 <= 0:
            raise ValueError("Числа должны быть натуральными.")
        custom_result = gcd_custom(num1, num2)
        math_result = math.gcd(num1, num2)
        print(f"НОД (ваш алгоритм): {custom_result}")
        print(f"НОД (math.gcd): {math_result}")
    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

if __name__ == "__main__":
    calculate_gcd()

