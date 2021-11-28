name = input('Введите имя: ')
lastname = input('Введите фамилию: ')
age = int(input('Введите возраст: '))
weight = int(input('Введите вес: '))

if age <= 30 and 50 <= weight <= 120:
    print(lastname, name, ', возраст:', age, ', вес:', weight, '- хорошее состояние!')
elif 30 < age <= 40 and (weight < 50 or weight > 120):
    print(lastname, name, ', возраст:', age, ', вес:', weight, '- следует заняться собой!')
else:
    print(lastname, name, ', возраст:', age, ', вес:', weight, '- следует обратиться к врачу!')
