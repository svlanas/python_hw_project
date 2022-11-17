import random
lst = [random.randint(1, 100) for i in range(15)]
if sum(j for j in lst if j % 2 != 0) > sum(j for j in lst if j % 2 == 0):
    print("Так")
else:
    print("Ні")
    