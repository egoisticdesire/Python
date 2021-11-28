# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и
# разрядность вашей ОС.

from sys import getsizeof

num_1 = input('Число: ')

even_number_count = sum(1 for i in num_1 if int(i) % 2 == 0)
odd_number_count = sum(1 for i in num_1 if int(i) % 2 != 0)

# print(f'{even_number_count} четных цифры: {", ".join(i for i in num_1 if int(i) % 2 == 0)} \n'
#       f'{odd_number_count} нечетных цифры: {", ".join(i for i in num_1 if int(i) % 2 != 0)}')

print(getsizeof(num_1))
print(getsizeof(even_number_count))
print(getsizeof(", ".join(i for i in num_1 if int(i) % 2 == 0)))

'''
1) строка
2) целое число
3) строка

Python (3.10), Win (x64)
'''