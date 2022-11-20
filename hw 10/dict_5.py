string = 'python is good language to code'
keys = set(string)
keys.remove(" ")
values = []
for i in keys:
    values.append(string.count(i))
dct = dict(zip(keys, values))
print("Dictionary of the number of characters in a sentence \n", dct)
