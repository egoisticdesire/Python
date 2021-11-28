n = None

while True:
    n = int(input('Введите число: '))
    if 0 < n < 10:
        print('Введенное число в степени 2 равно', n ** 2)
        break
    else:
        print('Число должно быть в диапазоне от 0 до 10!')
