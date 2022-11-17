n = int(input("Введіть розмір квадратної матриці "))
mtx = [
    [i for i in range(-n, 0)] if j % 2 == 0
    else [j + 1 for _ in range(n)]
    for j in range(n)
]
for r in range(n):
    for c in range(n):
        print('{:3d}'.format(mtx[r][c]), end="")
    print()
