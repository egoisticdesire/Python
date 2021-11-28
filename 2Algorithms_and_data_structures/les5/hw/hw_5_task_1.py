# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и
# отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import defaultdict, deque

count_companies = int(input('количество компаний: '))
companies = defaultdict()
max_profit_comp = deque()
min_profit_comp = deque()
sum_profit = 0
QUARTER = 4

for i in range(count_companies):
    name_company = input(f'название {i + 1} компании: ')
    profit = 0
    q = 1
    while q <= QUARTER:
        profit += float(input(f'прибыль за {q} квартал: '))
        q += 1
    companies[name_company] = profit
    sum_profit += profit

avrg_profit = sum_profit / count_companies

for k, v in companies.items():
    if v >= avrg_profit:
        max_profit_comp.append(k)
    else:
        min_profit_comp.append(k)

print('Прибыль выше среднего:')
for name in max_profit_comp:
    print(name)
print('Прибыль ниже среднего:')
for name in min_profit_comp:
    print(name)
