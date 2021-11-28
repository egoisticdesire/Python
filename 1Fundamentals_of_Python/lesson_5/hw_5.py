src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


# Вариант_1: это решение считается  решением "в лоб"?
def unique_nums(arr):
    result = []
    for i in arr:
        if arr.count(i) == 1:
            result.append(i)
    return result


print('Вариант_1:', unique_nums(src))


# Вариант_2
print('Вариант_2:', [i for i in src if src.count(i) == 1])
