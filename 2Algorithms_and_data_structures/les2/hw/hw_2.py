# # task_1
# while True:
#     num_1, num_2 = int(input('Первое число: ')), int(input('Второе число: '))
#     math_action = input('Выбери действие ("+", "-", "*", "/"). Для выхода нажми "0": ')
#
#     if math_action == '+':
#         print(num_1 + num_2)
#     elif math_action == '-':
#         print(num_1 - num_2)
#     elif math_action == '*':
#         print(num_1 * num_2)
#     elif math_action == '/':
#         if num_2 == 0:
#             print('На ноль делить нельзя!\n')
#         else:
#             print(num_1 / num_2)
#     elif math_action == '0':
#         exit(0)
#     else:
#         print('Ошибка ввода\n')
#
#########################################################
# # task_2
# num_1 = input('Число: ')
#
# even_number_count = sum(1 for i in num_1 if int(i) % 2 == 0)
# odd_number_count = sum(1 for i in num_1 if int(i) % 2 != 0)
#
# print(f'{even_number_count} четных цифры: {", ".join(i for i in num_1 if int(i) % 2 == 0)} \n'
#       f'{odd_number_count} нечетных цифры: {", ".join(i for i in num_1 if int(i) % 2 != 0)}')
#
#########################################################
# # task_3: перебор символов начиная с конца строки.
# # вариант, в котором число вводится с клавиатуры и является строкой:
# num_1 = input('Число: ')
# print(num_1[::-1])  # №1, побыстрее
# print(''.join(reversed(num_1)))  # №2, помедленнее
#
# # вариант, в котором задано именно число:
# num_1 = 12345
# print(str(num_1)[::-1])
# print(''.join(reversed(str(num_1))))
#
#########################################################
# # task_9
# def sum_digits(num):
#     return sum(int(i) for i in (str(num)))
#
#
# num_1, num_2, num_3 = 77778, 8888, 9999
#
# if sum_digits(num_1) > sum_digits(num_2) and \
#         sum_digits(num_1) > sum_digits(num_3):
#     print(f'Сумма цифр числа {num_1} равна '
#           f'{max(sum_digits(num_1), sum_digits(num_2), sum_digits(num_3))}')
#
# elif sum_digits(num_2) > sum_digits(num_1) and \
#         sum_digits(num_2) > sum_digits(num_3):
#     print(f'Сумма цифр числа {num_2} равна '
#           f'{max(sum_digits(num_1), sum_digits(num_2), sum_digits(num_3))}')
#
# elif sum_digits(num_3) > sum_digits(num_1) and \
#         sum_digits(num_3) > sum_digits(num_2):
#     print(f'Сумма цифр числа {num_3} равна '
#           f'{max(sum_digits(num_1), sum_digits(num_2), sum_digits(num_3))}')
# else:
#     print(f'Сумма цифр в некоторых числах равны и составляют '
#           f'{max(sum_digits(num_1), sum_digits(num_2), sum_digits(num_3))}')
