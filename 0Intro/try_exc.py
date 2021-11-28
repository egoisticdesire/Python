def range_number(result):
    if 0 < result < 100:
        try:
            if result == 13:
                raise ValueError('Введено число 13')
        except ValueError:
            print('Введено число 13')
        else:
            print('Число в квадрате: ', result ** 2)
    else:
        print('Число должно быть от 1 до 100!')


number = int(input('Введи число: '))
range_number(number)
