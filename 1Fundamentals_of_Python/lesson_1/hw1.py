duration = int(input('Введите число: '))
time_seconds = duration % 60
time_minutes = duration // 60 % 60
time_hours = duration // 3600 % 24
time_days = duration // 86400

if 0 < duration < 60:
    print(time_seconds, 'сек')
elif 60 <= duration < 3600:
    print(time_minutes, 'мин', time_seconds, 'сек')
elif 3600 <= duration < 86400:
    print(time_hours, 'час', time_minutes, 'мин', time_seconds, 'сек')
elif duration >= 86400:
    print(time_days, 'дн', time_hours, 'час', time_minutes, 'мин', time_seconds, 'сек')
else:
    print('Введите положительное число!')
