def sum_digits(value):
    result = 0
    while value != 0:
        result += value % 10
        value //= 10
    return result


qube_numbers_array = [i ** 3 for i in range(1, 1001, 2)]
qube_numbers_array_2 = [i ** 3 + 17 for i in range(1, 1001, 2)]
sum_numbers_1 = 0
sum_numbers_2 = 0
sum_numbers_3 = 0

# (a)
for number in qube_numbers_array:
    if sum_digits(number) % 7 == 0:
        sum_numbers_1 += number

# (b)
for number in qube_numbers_array_2:
    if sum_digits(number) % 7 == 0:
        sum_numbers_2 += number

# (c)
for number in range(len(qube_numbers_array)):
    qube_numbers_array[number] += 17
    if sum_digits(qube_numbers_array[number]) % 7 == 0:
        sum_numbers_3 += qube_numbers_array[number]

print('Результат (a): ', sum_numbers_1)
print('Результат (b): ', sum_numbers_2)
print('Результат (c): ', sum_numbers_3)
