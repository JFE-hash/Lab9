import json

with open('1.json', 'r', encoding='UTF-8') as json_file:
    data = json.load(json_file)

n = int(input('Сколько продуктов нужно добавить? - '))
for i in range(n):
    name = input('Название: ')
    price = int(input('Цена: '))
    weight = int(input('Вес: '))
    available = bool(input('В наличии (если нет, просто нажать Enter): '))
    print('')
    print(available)
    data['products'].append({'name': name, 'price': price, 'available': available, 'weight': weight})

with open('1.json', 'w', encoding='UTF-8') as file:
    json.dump(data, file)

for i in data['products']:
    print('Название:', i['name'])
    print('Цена:', i['price'])
    print('Вес:', i['weight'])
    if i['available']:
        print('В наличии')
    else:
        print('Нет в наличии!')
    print('')
