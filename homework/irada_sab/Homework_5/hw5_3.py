students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

# Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так:
# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography

a = ', '.join(students)
b = ', '.join(subjects)
for_sentence = 'Students {0}, study these subjects: {1}'

print(for_sentence.format(a, b))
