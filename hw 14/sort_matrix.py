def sort_matrix(m: int) -> list:
    """

    :param m: ціле число, задає розмір матриці
    :return: відсортовану матрицю m*m та суму кожного стовпця матриці
    """

    import random
    # генерація списку m*m
    l_1 = [[random.randint(0, 50) for _ in range(m)] for _ in range(m)]

    # генерація допоміжного списку із сум стовпців матриці
    l_2 = []
    for i in range(m):
        l_2.append(sum(l_1[j][i] for j in range(m)))

    # сортування стовпців матриці за зростанням суми їх значень
    for i in range(m):
        for j in range(m - 2, i-1, -1):
            if l_2[j] > l_2[j + 1]:
                l_2[j], l_2[j + 1] = l_2[j + 1], l_2[j]
                for k in range(m):
                    l_1[k][j], l_1[k][j + 1] = l_1[k][j + 1], l_1[k][j]

    # сортування значень всередені стовпців
    for i in range(m):
        for j in range(m):
            for k in range(m - 2, j-1, -1):
                if i % 2 != 0:
                    if l_1[k][i] > l_1[k + 1][i]:
                        l_1[k][i], l_1[k + 1][i] = l_1[k + 1][i], l_1[k][i]
                else:
                    if l_1[k][i] < l_1[k + 1][i]:
                        l_1[k][i], l_1[k + 1][i] = l_1[k + 1][i], l_1[k][i]

    # виведення в консоль відформатованої відсотртованої матриці m*m та суми
    # значень стовпців
    l_1 = l_1 + [l_2]
    for u in range(m + 1):
        for v in range(m):
            print('{:4d}'.format(l_1[u][v]), end="")
        print()
    return


if __name__ == '__main__':
    m = int(input("Введіть розмір квадратної матриці (має бути більше 5) "))
    while m <= 5:
        print("Розмір матриці має бути більшим 5")
        m = int(input("Введіть розмір квадратної матриці (має бути більше 5) "))
    sort_matrix(m)
