person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
# name, last_name, city, phone, country
name = person[0]
last_name = person[1]
city = person[2]
phone = person[3]
country = person[4]
print(name, last_name, city, phone, country)

# С помощью срезов и метода index получите из каждой строки с результатом число,
# прибавьте к полученному числу 10, результат сложения распечатайте.
str1 = 'результат операции: 42'
str2 = 'результат операции: 514'
str3 = 'результат работы программы: 9'

colon1 = str1.index(':')
colon2 = str2.index(':')
colon3 = str3.index(':')

number_str1 = str1[colon1 + 1:].strip()
number_str2 = str2[colon2 + 1:].strip()
number_str3 = str3[colon3 + 1:].strip()

number1 = int(number_str1)
number2 = int(number_str2)
number3 = int(number_str3)
new_number1 = number1 + 10
new_number2 = number2 + 10
new_number3 = number3 + 10

print(new_number1, new_number2, new_number3)

students = ['Ivanov', 'Petrov', 'Sidorov']
a = students[0]
b = students[1]
c = students[2]
subjects = ['math', 'biology', 'geography']
d = subjects[0]
e = subjects[1]
f = subjects[2]
# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography
my_text = 'Students {}, {}, {} study these subjects: {}, {}, {}'
print(my_text.format(a, b, c, d, e, f))
