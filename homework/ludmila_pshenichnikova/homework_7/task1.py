
i = 5

while True:
    user_input = int(input('Guess the number!'))
    if user_input != i:
        print('Try again')
        continue
    elif user_input == i:
        print('Сongratulations, you guessed it right')
        break
