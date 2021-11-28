import pickle
import json

# pickle
print('Pickle')
with open('group.pickle', 'rb') as f:
    group_list = pickle.load(f)

print(group_list)
print(type(group_list))

print('-' * 50)

# json
print('Json')
with open('group.json', 'r', encoding='utf-8') as f:
    group_list = json.load(f)

print(group_list)
print(type(group_list))
