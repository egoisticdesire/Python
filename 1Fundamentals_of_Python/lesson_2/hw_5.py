prices = [22.2, 44.4, 11.1, 66.6, 111, 77.7, 33.3, 88.8, 55.5, 99.9]

# (a)
for price in prices:
    rub = int(price)
    kk = (price - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп')

# (b)
prices = [22.2, 44.4, 11.1, 66.6, 111, 77.7, 33.3, 88.8, 55.5, 99.9]

print()  # разделитель для удобства чтения результата
print('id1:', id(prices))
prices.sort()
print('id2:', id(prices))
for price in prices:
    rub = int(price)
    kk = (price - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп')

# (c)
prices = [22.2, 44.4, 11.1, 66.6, 111, 77.7, 33.3, 88.8, 55.5, 99.9]

print()
for price in list(reversed(sorted(prices))):
    rub = int(price)
    kk = (price - rub) * 100
    print(f'{rub} руб {kk:02.0f} коп')

# (d)
prices = [22.2, 44.4, 11.1, 66.6, 111, 77.7, 33.3, 88.8, 55.5, 99.9]

"""
По условию задачи нужно вывести цены по возрастанию, а в Вашем решении было по убыванию.
Добавил list(reversed()). Условие задачи стало выполняться.
"""
print()
print(list(reversed(
    [f'{int(price)} руб {(price - int(price)) * 100:02.0f} коп' for price in sorted(prices)[::-1][:5]])))
