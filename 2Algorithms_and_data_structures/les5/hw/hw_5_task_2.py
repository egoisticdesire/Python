# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число
# представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл
# A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера:
# [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

# a = ['A', '2']  # 'A2'
# b = ['C', '4', 'F']  # 'C4F'

num_1 = list(input('first number: ').upper())
num_2 = list(input('second number: ').upper())
sum_result = hex(int(''.join(num_1), 16) + int(''.join(num_2), 16)).removeprefix('0x')
mult_result = hex(int(''.join(num_1), 16) * int(''.join(num_2), 16)).removeprefix('0x')

print(f'\nnum_1 = {num_1}\nnum_2 = {num_2}')
print(f'\nsum_result = {list(sum_result.upper())}')
print(f'mult_result = {list(mult_result.upper())}')
