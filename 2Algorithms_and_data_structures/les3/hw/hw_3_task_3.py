# task_3
from random import randint

my_list = [randint(-9, 9) for i in range(9)]

a = my_list.index(min(my_list))
b = my_list.index(max(my_list))

print(my_list)
print(min(my_list))
print(max(my_list))

my_list[a], my_list[b] = my_list[b], my_list[a]

print(my_list)
