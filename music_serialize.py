import json, pickle, os

my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': ['Последний есяц осени', 'Шапито'],
    'Albums': [
        {'name': 'Делать панк-рок', 'year': 2016},
        {'name': 'Шапито', 'year': 2014}
    ]
}

file_path_1 = os.path.join(os.path.dirname(__file__), 'group.json')
file_path_2 = os.path.join(os.path.dirname(__file__), 'group.pickle')

with open(file_path_1, 'w', encoding='UTF-8') as file:
    json.dump(my_favourite_group, file)

with open(file_path_2, 'wb') as file:
    pickle.dump(my_favourite_group, file)

print('Done')
