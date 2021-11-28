import sys
from itertools import zip_longest, islice

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий',
          'Борис', 'Елена', 'Геннадий', 'Степан', 'Варвара']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

result = ((name, num) for name, num in zip_longest(tutors, classes[:len(tutors)]))

print(*islice(result, sys.maxsize), sep='\n')
print(type(result))
