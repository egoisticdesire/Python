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
def eratosthenes():  # сложность O(n log(log n))
    sieve = list(range(9999))
    sieve[1] = 0
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return [x for x in sieve if x != 0]


@time_func
def not_eratosthenes():  # сложность O(n^2)
    lst = []
    for i in range(2, 9999):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


eratosthenes()
not_eratosthenes()
