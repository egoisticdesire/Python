list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6, -7, -8, -9]
result = []

# Элемент кратен 3
result = [i for i in list1 if i % 3 == 0]
print(result)

# Элемент положительный
result = [i for i in list1 if i > 0]
print(result)

# Элемент не кратен 4
result = [i for i in list1 if i % 4 != 0]
print(result)

# Результат, учитывающий все 3 условия
result = [i for i in list1 if i > 0 and i % 3 == 0 and i % 4 != 0]
print(result)
