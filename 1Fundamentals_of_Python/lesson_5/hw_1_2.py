import sys
from itertools import islice


# task_1


def num_gen(max_num):
    yield from range(1, max_num + 1, 2)  # записать из диапазона()


print(list(num_gen(5)))
try:
    next_hop = num_gen(5)
    print(next(next_hop))
    print(next(next_hop))
    print(next(next_hop))
    print(next(next_hop))  # вызывает ошибку из-за превышения диапазона
except StopIteration:
    print('StopIteration')

# task_2*

max_numb = 5
num_gen_2 = (i for i in range(1, max_numb + 1, 2))
# print([i for i in range(1, max_numb + 1, 2)])
print(*islice(num_gen_2, sys.maxsize), sep='\n')
