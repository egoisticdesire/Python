import pickle
import json

group_list = {
    'name': 'Anacondaz',
    'tracks': ['Уходи', 'Серым'],
    'albums': [{
        'name': 'Эволюция', 'year': 2011,
        'name': 'Перезвони мне..', 'year': 2020
    }]
}

p_group = pickle.dumps(group_list)
print(p_group)
j_group = json.dumps(group_list)
print(j_group)

# pickle
with open('group.pickle', 'wb') as f:
    pickle.dump(group_list, f)

# json
with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(group_list, f)
