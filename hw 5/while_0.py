n = int(input("введіть число "))
count = 0
sum_ = 0
med_ = 0
max_ = n
min_ = n
count_even = 0
count_odd = 0
while n != 0:
    count += 1
    sum_ = sum_ + n
    med_ = sum_ / count
    if n > max_:
        max_ = n
    if n < min_:
        min_ = n
    if n % 2 == 0:
        count_even += 1
    else:
        count_odd += 1
    n = int(input("введіть ще число "))
print("\n Сумма введених числе =", sum_, "\n Середнє арифметичне введених чисел =", med_,
      "\n Максимальне значення серед введених чисел =", max_, "\n Мінімальне значення серед введених чисел =", min_,
      "\n Кількість парних чисел =", count_even, "\n Кількість непарних чисел =", count_odd)
