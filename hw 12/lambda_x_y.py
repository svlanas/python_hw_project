import random
func = lambda x, y=1: x ** y
lst_1 = [random.randint(0, 100) for i in range(5)]
lst_2 = [j for j in range(1, 13, 2)]
res_1 = list(map(func, lst_1))
res_2 = list(map(func, lst_1, lst_2))
print(res_1)
print(res_2)
