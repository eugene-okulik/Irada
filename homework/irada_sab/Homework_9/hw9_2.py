# Map, filter:
# С помощью функции map или filter создайте из этого списка новый список с жаркими днями.
# жарким всё, что выше 28.
# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29,
                25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

hot_temp = []

for c in temperatures:
    if c > 28:
        hot_temp.append(c)

print(hot_temp)
print(f'Maximum temperature is {max(hot_temp)}')
print(f'Minimum temperature is {min(hot_temp)}')


total_temp = sum(hot_temp)
qty_elem = len(hot_temp)

if qty_elem > 0:
    average = total_temp / qty_elem
    print(f'Average temperature is {round(average, 2)}')
