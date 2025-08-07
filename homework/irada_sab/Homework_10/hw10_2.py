# Создайте универсальный декоратор, который будет управлять тем, сколько раз запускается декорируемая функция:
# @repeat_me
# def example(text):
#     print(text)
#
# example('print me', count=2)
#
# В результате работы будет такое:
# print me
# print me

def repeat_me(func):
    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)

        for x in range(count):
            func(*args, **kwargs)

    return wrapper


@repeat_me
def my_func(forargs):
    print(forargs)


my_func('print me', count = 2)
my_func('test')
