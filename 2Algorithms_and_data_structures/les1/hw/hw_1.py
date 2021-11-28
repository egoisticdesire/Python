# task_1
print('task_1')

# num1 = int(input('number1: '))
# num2 = int(input('number2: '))
# num3 = int(input('number3: '))
num1, num2, num3 = map(int, input('введи три числа через пробел: ').split())

print(f'sum_result = {num1 + num2 + num3}\n'
      f'multiply_result = {num1 * num2 * num3}')

# task_2
# Логические побитовые операции выполняются с двоичной формой числа
# Например, при логическом И получится "1" только при всех "1", т.е.
# 5 = 101       1 И 0 = 0
# 6 = 110       0 И 1 = 0
#               1 И 1 = 1
#               Результат: 100, что равняется числу 4
# При сдвиге влево фактически дописываются нули справа (умножение)
# При сдвиге вправо фактически дописываются нули слева, которые в итоге не учитываются (деление нацело)
print('\ntask_2')

a = 5
b = 6
print(f'{a} = {bin(a)} \n'
      f'{b} = {bin(b)} \n'
      f'{a} & {b} = {a & b} ({bin(a & b)}) \n'
      f'{a} | {b} = {a | b} ({bin(a | b)}) \n'
      f'{a} ^ {b} = {a ^ b} ({bin(a ^ b)}) \n'
      f'{a} << 2 = {a << 2} ({bin(a << 2)}) \n'
      f'{a} >> 2 = {a >> 2} ({bin(a >> 2)})')

# task_7
print('\ntask_7')

# side_a = int(input('первая сторона: '))
# side_b = int(input('вторая сторона: '))
# side_c = int(input('третья сторона: '))
side_a, side_b, side_c = map(int, input('введи стороны треугольника через пробел: ').split())

if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
    if side_a == side_b == side_c:
        print('равносторонний треугольник')
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        print('равнобедренный треугольник')
    else:
        print('разносторонний треугольник')
else:
    print('ни разу не треугольник!')

# task_9
print('\ntask_9')

# num1 = int(input('number1: '))
# num2 = int(input('number2: '))
# num3 = int(input('number3: '))
num1, num2, num3 = map(int, input('введи три числа через пробел: ').split())

avr = num1
if num2 > avr > num3 or num3 > avr > num2:
    print(f'result: {avr}')
else:
    avr = num2
    if num1 > avr > num3 or num3 > avr > num1:
        print(f'result: {avr}')
    else:
        avr = num3
        print(f'result: {avr}')
