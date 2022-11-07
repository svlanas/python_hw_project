str = input("Введіть рядок ")
char = input("Введіть символ ")
l = len(str)
i = 0
while i < l:
    i = str.find(char, i)
    print(i)
    i += 1