from collections import Counter

def find_mode(array):
    try:
        if not array:
            raise ValueError("Массив пуст.")
        counts = Counter(array)
        max_frequency = max(counts.values())
        modes = [key for key, count in counts.items() if count == max_frequency]
        if len(modes) > 1:
            raise ValueError("Массив не имеет моды, так как наиболее часто встречается несколько элементов.")
        return modes[0]
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

def main():
    try:
        print("Введите массив целых чисел через пробел:")
        array = list(map(int, input().split()))
        mode = find_mode(array)
        if mode is not None:
            print(f"Мода массива: {mode}")
    except Exception as e:
        print(f"Ошибка ввода данных: {e}")

if __name__ == "__main__":
    main()
