import random


def prime_numbers(a, b):
    """

    :param a: початок діапазону
    :param b: кінець діапазону
    :return: прості числа із вказаного діапазону
    """
    for i in range(a, b):
        # для кожного i з діапазону від а до b формую списки перевірок
        # рівності 0 остачі від ділення і на кожне число з діпазону від 2 до і-1
        # для i = 2 цикл не виконується
        lst = []
        for j in range(2, i):
            lst.append(i % j == 0)
        # якщо жодне значення з такого списку не дорівнює True - число є
        # простим,при цьому і>2 або i == 2
        if not any(lst) and (i > 2) or i == 2:
            yield i


n = random.randint(1, 1000)
z = random.randint(n + 1, 1001)
for k in prime_numbers(n, z):
    print(k, end=" ")
