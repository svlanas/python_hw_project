dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_1_2 = dict(**dictionary_1, **dictionary_2)
print("United dictionary:", dictionary_1_2)
