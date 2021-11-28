# name = input('Имя: ')
# age = int(input('Возраст: '))
# city = input('Город: ')
# # print('{}, {} год(а), проживает в городе {}'.format(name, age, city))
# print(f'{name}, {age} год(а), проживает в городе {city}')


def big_data(name, age, city):
    return f'{name}, {age} год(а), проживает в городе {city}'


name = input('Имя: ')
age = input('Возраст: ')
city = input('Город: ')

print(big_data(name, age, city))
