my_dict = {'tuple': (1,7,79,53,'test'),
           'list': [25, 8, -4, 'python', 2],
           'dict': {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
           'set': {55, 'text', 1, 2, 7}}
#выведите на экран последний элемент
my_dict['tuple'][-1]

#добавьте в конец списка еще один элемент
my_dict['list'].append(10)
#удалите второй элемент списка
my_dict['list'].pop(1)

#добавьте элемент с ключом ('i am a tuple',) и любым значением
my_dict['dict'][('i am a tuple',)] = 'some value'
#удалите какой-нибудь элемент
my_dict['dict'].pop('three')

#добавьте новый элемент в множество
my_dict['set'].add(100)
#удалите элемент из множества
my_dict['set'].pop()

print(my_dict)
