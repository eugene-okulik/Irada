# дата: "Jan 15, 2023 - 12:05:33"    Преобразуйте эту дату в питоновский формат:
# 1. Распечатайте полное название месяца из этой даты
# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"

import datetime

my_date = 'Jan 15, 2023 - 12:05:33'

pyth_format = datetime.datetime.strptime(my_date, '%b %d, %Y - %H:%M:%S')

print(pyth_format.strftime('%B'))
print(pyth_format.strftime('%d.%m.%Y, %H:%M'))
