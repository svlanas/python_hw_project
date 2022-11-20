import random
number_list = len(set([random.randint(-100, 100) for i in range(100)]))
print("Number of unique values in list:", number_list)
