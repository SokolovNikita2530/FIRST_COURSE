import json

def get_animals_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Error reading file: {e}')
        return []

def filter_birds(animals):
    birds = list(filter(lambda x: x.get('class') == 'Bird', animals))
    print('Birds:')
    for bird in birds:
        print(bird)

def count_diurnal_animals(animals):
    diurnal_count = len(list(filter(lambda x: x.get('activity') == 'Diurnal', animals)))
    print(f'Number of diurnal animals: {diurnal_count}')

def find_lightest_animal(animals):
    try:
        lightest = min(animals, key=lambda x: x.get('weight_min', float('inf')))
        print('Animal with the lowest minimum weight:')
        print(lightest)
    except ValueError:
        print('Animal list is empty.')

if __name__ == '__main__':
    path = input('Enter the path to animals.json: ')
    animals_data = get_animals_data(path)
    if animals_data:
        filter_birds(animals_data)
        count_diurnal_animals(animals_data)
        find_lightest_animal(animals_data)
