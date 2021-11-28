# # list1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# # list2 = {1, 3, 5, 7, 9}
# #
# # print(list1 - list2)
#
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [1, 3, 5, 7, 9]
#
# res = []
#
# for i in list1:
#     if i not in list2:
#         res.append(i)
#
# print(res)

list1 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1, 3, 5, 7, 9]
res = []

for i in list1[:]:
    if i not in list2:
        res.append(i)

print(res)
