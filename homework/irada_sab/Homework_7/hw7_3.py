# Получите из каждой строки с результатом число, прибавьте к полученному числу 10,
# выполните всё с использованием функций.

fresult = 'operation result: 42'
sresult = 'operation result: 54'
fprogram = 'result of programs work: 209'
lresult = 'result: 2'

def my_function(text, add_num=10):
    find_index = text.index(':')
    my_number = int(text[find_index + 2:])
    return my_number + add_num


print(my_function(fresult, 20))
print(my_function(sresult))
print(my_function(fprogram))
print(my_function(lresult))

