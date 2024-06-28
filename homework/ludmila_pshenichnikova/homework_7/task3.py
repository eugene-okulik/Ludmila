str1 = 'результат операции: 42'
str2 = 'результат операции: 54'
str3 = 'результат работы программы: 209'
str4 = 'результат: 2'
main_number = 10

def final(*args):
    number = int(args.split()[-1])
    result = 0
    for number in args:
        result = number + main_number
        return result
    print(final(args))
