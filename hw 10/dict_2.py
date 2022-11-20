import random
dct = {i: random.randint(1, 4) for i in range(1, 21)}
lst_values = list(dct.values())
prod = 1
for j in range(len(lst_values)):
    prod = prod * lst_values[j]
    j += 1
print("Dictionary:", dct)
print("Product of dictionary's values:", prod)
