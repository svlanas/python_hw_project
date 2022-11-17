import random
n = int(input("Введіть розмір квадратної матриці "))
mtx = [[random.randint(1, 100) for i in range(n)] for j in range(n)]
for i in range(n):
    print(mtx[i])
print("сума чисел по діагоналі =", sum(mtx[i][i] for i in range(n)))
print("сума чисел остнанього стовбця =", sum(mtx[i][n-1] for i in range(n)))
