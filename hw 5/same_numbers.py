# n = input("Введіть число ")
# for i in range(10):
#     # перевіряємо кількість кожної цифри в введеному числі, допоки не знайдемо кількість > 1
#     if n.count(str(i)) > 1:
#         print("Число містить однакові цифри")
#         break
#     i += 1

# else:
#     print("Число не містить однакових цифр")

n = input("Введіть число ")
# визначаю кількість цифр у введеному числі
k = 0
x = int(n)
while x > 0:
    x //= 10
    k += 1
# цикл для перевірки цифр від 0 до 9
dig = 0
while dig < 10:
    # рахую скільки разів зустрічається цифра у введеному числі
    count = 0
    for i in range (0, k):
        if str(dig) == n[i]:
            count += 1
    # якщо лічильник кількості цифр - більше 1 - зупинити цикл і вивести повідомлення
    if count > 1:
        print("Число містить однакові цифри")
        break
    dig += 1
else:
    print("Число не містить однакових цифр")

