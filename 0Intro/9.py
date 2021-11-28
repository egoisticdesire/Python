numbers = []


def max_number():
    return max(numbers)


for i in range(3):
    number = int(input('Введите число: '))
    numbers.append(number)

print(max_number())
