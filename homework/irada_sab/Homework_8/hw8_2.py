# функцию-генератор, генерирует бесконечную последовательность чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число
# На всякий случай, напомню, что превращать результат работы генератора в список - неправильно.

def fibonacci():
    num_a, num_b = 0, 1
    while True:
        yield num_a
        num_a, num_b = num_b, num_a + num_b

def find_fibo(*my_num):
    fib_num = fibonacci()
    max_num = max(my_num)
    for indx, num in enumerate(fib_num):
        if indx in my_num:
            print(f"The {indx}th Fibonacci number is: {num}")
        if indx >= max_num:
            break

# Can't print the 100000th Fibonacci numbers :(
find_fibo(5, 200, 1000, 100000)
