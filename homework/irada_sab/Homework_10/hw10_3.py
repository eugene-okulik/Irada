# Есть функция которая делает одну из арифметических операций
# с переданными ей числами (числа и операция передаются в аргументы функции) примерно:
# def calc(first, second, operation):
#     if operation == '+':
#         return first + second
#     elif .....
# Программа спрашивает у пользователя 2 числа (вне функции)
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение


def decor_func(func):
    def wrapper(first, second, operation=None):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'

        return func(first, second, operation)

    return wrapper


@decor_func
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return second / first
    elif operation == '*':
        return first * second


first_number = float(input('Enter the first number: '))
second_number = float(input('Enter the second number: '))

result = calc(first_number, second_number)

print(f'Result: {result}')
