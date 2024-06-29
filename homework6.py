# Словари
my_dict = {'Apple': 'Яблоко', 'Peach': 'Персик', 'Banana': 'Банан'}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Apple'])   # Вывод на экран значения по существуюшему ключу
print('Not existing value: ', my_dict.get('Grape'))  # Проверка на существование объекта
my_dict.update({'Plum': 'Слива', 'Pumpkin': 'Тыква'})  # Добавление двух новых объектов (пар)
print('Deleted value: ', my_dict.pop('Peach'))  # Удаление одного из существующих объектов
print('Modified dictionary: ', my_dict)

# Множества
my_set = {1, 2, 2, 7, True, False, True, 'stop'}
print('Set: ', my_set)
(my_set.add(9), my_set.add('run'), my_set.discard(1))
print('Modified set: ', my_set)
