# task_7
from random import randint

my_list = [randint(-100, 100) for i in range(100)]
print(*sorted(my_list)[:2])
