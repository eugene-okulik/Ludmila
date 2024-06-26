text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl,'
        ' facilisis vitae semper at, dignissim vitae libero')
words = text.split()

for word in words:
    if word[-1] in ',.':
        a = word[-1]  # Сохраняем знак препинания
        word = word[:-1] + 'ing' + a
    else:
        word += 'ing'
    print(word, end=' ')
