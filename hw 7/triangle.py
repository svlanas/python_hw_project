n = input("Input number ")
while n.isdigit() != True:
    print("It's not number!")
    n = input("Input number ")
else:
    n2 = int(n)
    for i in range(n2):
        print(f"{i:>{len(n)}} {10**i:>{n2}}")


