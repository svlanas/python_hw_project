str = input("Введіть рядок ")
char = input("Введіть символ ")
l = len(str)
i = 0
while i < l:
    i = str.find(char, i)
    if i == -1:
        break
    print(i)
    i += 1