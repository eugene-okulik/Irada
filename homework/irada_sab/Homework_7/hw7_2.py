# Выведите на экран каждый ключ столько раз сколько указано в значении.

words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for key, value in words.items():
    print(key * value)
