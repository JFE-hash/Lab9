import json

with open('1.json', 'r', encoding='UTF-8') as json_file:
    data = json.load(json_file)

for i in data['products']:
    print('Название:', i['name'])
    print('Цена:', i['price'])
    print('Вес:', i['weight'])
    if i['available']:
        print('В наличии')
    else:
        print('Нет в наличии!')
    print('')
