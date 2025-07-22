# переменные Salary - int, bonus - bool. Спросите у пользователя salary.
# Если bonus - true, то к salary должен быть добавлен рандомный бонус.
# Примеры результатов:
# 10000, True - '$10255'
# 25000, False - '$25000'
# 600, True - '$3785'

import random

salary = int(input("What is your salary? "))
bonus = random.choice([True, False])
my_bonus = int(random.randint(100, 5000))

if bonus == True:
    print(f" {salary}, {bonus} - '${salary + my_bonus}'")
else:
    print(f" {salary}, {bonus} - '${salary}'")
