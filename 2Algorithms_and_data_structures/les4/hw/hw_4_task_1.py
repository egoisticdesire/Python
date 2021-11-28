from random import randint
import time


def time_func(func):
    def wrapper():
        start_time = time.time()
        res = func()
        end_time = time.time()
        print('Время исполнения', end_time - start_time)
        return res

    return wrapper


@time_func
def sort_rand():  # O(n log (n))
    return sorted([randint(-100000, 100000) for _ in range(100000)])[:2]


@time_func
def sort_rand_2():
    lst = []
    for _ in range(100000):
        lst.append(randint(-100000, 100000))
    return sorted(lst)[:2]


print(*sort_rand())
print(*sort_rand_2())

'''
# [randint(-100, 100) for _ in range(n)]

Иначе запишется, как:
# for _ in range(n):
#     list.append(randint(-100, 100))

Значит это O(n).

Сортировка имеет временную сложность O(n log n).

Итоговая сложность равна O(n log n)
'''
