def common_elements(set1, set2):
    if not all(isinstance(i, int) for i in set1) or not all(isinstance(i, int) for i in set2):
        raise ValueError("Оба набора должны содержать только числа.")
    return set1 & set2

def main():
    try:
        set1 = set(map(int, input("Введите числа первого набора (через пробел): ").split()))
        set2 = set(map(int, input("Введите числа второго набора (через пробел): ").split()))
        print(f"Числа, которые встречаются в обоих наборах: {common_elements(set1, set2)}")
    except ValueError as e:
        print(f"Ошибка: {e}")

