try:
    n = int (input ("Задайте число школярів: "))
    k = int (input("Задайте число яблук: "))
    if n < 0:
        print("Кількість школярів не може бути від'ємною")
    elif k < 0:
        print("Кількість яблук не може бути від'ємною")
    else:
        appl_pupil = k // n
        appl_basket = k % n
        print("1. Кожному школяру дісталося яблук: ", appl_pupil, "\n2. Яблук залишилось в корзинці: ", appl_basket)
except ValueError:
    print("Введене значення не є цілим числом")

