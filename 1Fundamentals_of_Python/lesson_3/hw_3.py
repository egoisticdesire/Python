def thesaurus(*names):
    result = {}
    for name in names:
        # key = name[0].title()
        # if key not in result:
        #     result[key] = []
        # result[key].append(name)
        result.setdefault(name[0], [])
        result[name[0]].append(name)
    return result


print(thesaurus('Вася', 'Петя', 'Паша', 'Макс', 'Вера'))
