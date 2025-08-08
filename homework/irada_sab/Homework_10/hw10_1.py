# Декоратор должен распечатывать "finished" после выполнения декорированной функции.
# Код, использующий этот декоратор может выглядеть, например, так:
# @finish_me
# def example(text):
#     print(text)

# example('print me')
# В результате работы будет такое:
# print me
# finished

def decor_func(func):
    def wrapper():
        func()
        print('Decorator finished')
    return wrapper


@decor_func
def my_func():
    print('Printing something from my function')


my_func()
