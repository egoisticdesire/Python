# task_4
from random import randint
from collections import Counter

my_list = [randint(-1, 1) for i in range(10)]
print(f'Список:\n{my_list}')  # для проверки (подсчета)
max_count = list(*Counter(my_list).most_common(1))
print(f'Цифра {max_count[0]} встречается в списке чаще остальных: {max_count[1]} раз(а)')
