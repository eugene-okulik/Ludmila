str1 = 'результат операции: 42'
str2 = 'результат операции: 54'
str3 = 'результат работы программы: 209'
str4 = 'результат: 2'
main_number = 10


def final(*args):
    results = []
    for arg in args:
        number = int(arg.split()[-1])
        result = number + main_number
        results.append(result)
    return results


print(final(str1, str2, str3, str4))
