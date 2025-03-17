import csv

def read_countries(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
        return data
    except FileNotFoundError as e:
        print(f'File not found: {e}')
        return []

def filter_by_income(countries, min_income, max_income):
    try:
        filtered = list(filter(
            lambda x: min_income <= float(x[2]) <= max_income,
            countries
        ))
        return filtered
    except (ValueError, IndexError):
        print('Error in CSV data.')
        return []

def sort_by_inflation(countries):
    try:
        sorted_list = sorted(countries, key=lambda x: float(x[3]))
        return sorted_list
    except (ValueError, IndexError):
        print('Error in CSV data.')
        return []

def write_csv(file_path, data):
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f'File successfully written: {file_path}')
    except Exception as e:
        print(f'Error writing file: {e}')

if __name__ == '__main__':
    path = input('Enter the path to countries.csv: ')
    countries_data = read_countries(path)
    if countries_data:
        try:
            min_income = float(input('Enter minimum income: '))
            max_income = float(input('Enter maximum income: '))
        except ValueError:
            print('Invalid income input.')
        else:
            filtered_countries = filter_by_income(countries_data, min_income, max_income)
            write_csv('countries_income_filtered.csv', filtered_countries)

            sorted_countries = sort_by_inflation(countries_data)
            write_csv('countries_sorted_inflation.csv', sorted_countries)
