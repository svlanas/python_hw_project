lst = list(range(10, 251))
for i in lst:
    if i % 20 == 0:
        lst.remove(i)
    i += 1
print(lst)
