def unique_in_first_string(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Обе строки должны быть строками.")
    
    # Преобразуем строки в множества
    set1 = set(str1)
    set2 = set(str2)
    
    # Разность множеств: символы из первой строки, которых нет во второй
    result = set1 - set2
    
    return result

# Ввод строк пользователем
try:
    string1 = input("Введите первую строку: ")
    string2 = input("Введите вторую строку: ")
    print(f"Символы, которые встречаются в первой строке, но не во второй: {unique_in_first_string(string1, string2)}")
except ValueError as e:
    print(f"Ошибка: {e}")
