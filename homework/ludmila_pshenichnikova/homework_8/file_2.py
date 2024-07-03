def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
number_5 = 0
number_200 = 0
number_1000 = 0
number_100000 = 0

counter = 0
for number in fibonacci_generator():
    if counter == 4:
        number_5 = number
    elif counter == 199:
        number_200 = number
    elif counter == 999:
        number_1000 = number
    elif counter == 99999:
        number_100000 = number
        break
    counter += 1
print(f'Пятое число: {number_5}')
print(f'Двухсотое число: {number_200}')
print(f'Тысячное число: {number_1000}')
# print(f'Стотысячное число: {number_100000}')
