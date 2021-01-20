import json, pickle

with open('group.json', 'r', encoding='UTF-8') as file:
    loaded_list_1 = json.load(file)
    print(loaded_list_1)

with open('group.pickle', 'rb') as file:
    loaded_list_2 = pickle.load(file)
    print(loaded_list_2)
