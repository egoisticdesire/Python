fruits1 = ['яблоки', 'бананы', 'помидоры', 'огурцы', 'картоха']
fruits2 = ['яблоки', 'тыква', 'перцы', 'огурцы', 'картоха']
result = []

# classic method
for fruit in fruits1:
    if fruit in fruits2:
        result.append(fruit)
print(result)


# generator
result = [fruit for fruit in fruits1 if fruit in fruits2]
print(result)
