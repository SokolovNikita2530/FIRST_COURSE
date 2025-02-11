def matrix_multiply(matrix1, matrix2):
    try:
        if len(matrix1[0]) != len(matrix2):
            raise ValueError("Количество столбцов первой матрицы не равно количеству строк второй матрицы.")
        result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]
        return result
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

def main():
    try:
        print("Введите первую матрицу построчно, числа через пробел (пустая строка для завершения):")
        matrix1 = []
        while (line := input().strip()):
            matrix1.append(list(map(float, line.split())))
        print("Введите вторую матрицу построчно, числа через пробел (пустая строка для завершения):")
        matrix2 = []
        while (line := input().strip()):
            matrix2.append(list(map(float, line.split())))
        result = matrix_multiply(matrix1, matrix2)
        if result is not None:
            print("Результат умножения:")
            for row in result:
                print(" ".join(map(str, row)))
    except Exception as e:
        print(f"Ошибка ввода данных: {e}")

if __name__ == "__main__":
    main()

