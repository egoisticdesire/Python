import math

list1 = [1, 4, 9, 16, 25, -1, -4, -9, -16, -25]


def new_list(input_list):
    input_list = input_list.copy()
    list_result = [int(math.sqrt(i)) if i > 0 else i for i in input_list]
    return list_result


print(list1)
print(new_list(list1))
