# task_5
# под "позицией" что понимать, индекс? если да, то решение ниже:
my_list = [1, 2, 5, 8, -1, -10, 0, -5]

max_negative_elem = max(i for i in my_list if i < 0)
print(f'Значение: {max_negative_elem}, позиция: {my_list.index(max_negative_elem)}')
# если нужна нумерация от 1, тогда решение следующее:
print(f'Значение: {max_negative_elem}, позиция: {my_list.index(max_negative_elem) + 1}')
