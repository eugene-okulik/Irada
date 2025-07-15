#  просит пользователя угадать цифру. Пользователь вводит цифру.
# Если цифры не равны: “попробуйте снова” и снова просит пользователя угадать цифру.
# Если пользователь угадывает цифру:“Поздравляю! Вы угадали!” и завершается.


my_number = 9

while True:
    if my_number == int(input('Guess my number! ')):
        print('Congrats! You guessed my number!')
        break
    else:
        print('Try again!')

print('Game is over!')

