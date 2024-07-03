import random

salary = int(input("Введите вашу зарплату: "))
bonus = random.choice([True, False])
if bonus == True:
    print(f'{salary}, {bonus} - ${random.randrange(1,250) + salary}')
else:
    print(f'{salary}, {bonus} - ${salary}')
