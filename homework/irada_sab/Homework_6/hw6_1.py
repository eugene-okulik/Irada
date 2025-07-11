""" добавляет ‘ing’ в конец слов (к каждому слову)и после этого выводит получившийся
текст на экран. Знаки препинания не должны оказаться внутри слова."""

my_text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
           'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
my_ing = 'ing'

all_words = my_text.split()
# print(all_words)

splits = []
for word in all_words:
    if word.endswith(',') or word.endswith('.'):
        new_word = word[:-1] + my_ing + word[-1]
    else:
        new_word = word + my_ing
    splits.append(new_word)

new_text = ' '.join(splits)    # Join with spaces

print(new_text)
