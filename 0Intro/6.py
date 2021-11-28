# Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.
# Примечание. Списки создайте вручную, например так:
# my_list_1 = [2, 2, 5, 12, 8, 2, 12]
#
# В этом случае ответ будет:
# [5, 8]

# list1 = [2, 2, 5, 12, 8, 2, 12]
# result = []
#
# for i in list1:
#     if i not in result:
#         result.append(i)
# print(result)
#
# result = set(list1)
#
# print(result)

# 1
list = [2, 2, 5, 12, 8, 2, 12]
result = []
for number in list:  # проверяем число в списке
    if list.count(number) == 1:  # кол-во одинаковых значений = 1
        result.append(number)  # записываем число в пустой список
print(result)

# 2
list1 = [2, 2, 5, 12, 8, 2, 12]
print([i for i in list1 if list1.count(i) == 1])
