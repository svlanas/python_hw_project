str = input("введіть число від 3 до 9 ")
if str.isdigit() != True or int(str) > 9 or int(str) < 3:
    print("Ви ввели некоректне значення!")
else:
    # left side
    for i in range(1, int(str) + 1):
        for n in range(1, i + 1):
            print(n, end="")
        for k in range(i - 1, 0, -1):
            print(k, end="")
        print()
    # center
    for i in range(1, int(str) + 1):
        for j in range(int(str), i, -1):
            print(end=" ")
        for n in range(1, i + 1):
            print(n, end="")
        for k in range(i - 1, 0, -1):
            print(k, end="")
        print()
    # right side
    for i in range(1, int(str) + 1):
        for j in range(int(str) * 2 - i, i, -1):
            print(end=" ")
        for n in range(1, i + 1):
            print(n, end="")
        for k in range(i - 1, 0, -1):
            print(k, end="")
        print()
