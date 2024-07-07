first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))


def new_decorator(func):
    def wrapper(first, second):
        print('function started')
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        if first < 0 or second < 0:
            operation = '*'
        result = func(first, second, operation)
        return result
    return wrapper


@new_decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return second - first
    elif operation == '*':
        return first * second
    elif operation == '/':
        if second != 0:
            return first / second
        else:
            return 'Division by zero is prohibited'
    else:
        return 'wrong'
fin_result = calc(first_number, second_number)


print(f'The result is: {fin_result}')
