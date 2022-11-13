lst_1 = [1, 2, 5, 7, 9, 99, 87, 200, 39, 2]
lst_2 = [5, 42, 29, 345, 50, 33, 7, 0, 201, 9, 2, 132, 45, 23,934]
print("{:<15}" "{:<15}".format("Element list1", "Count in list2"))
for i in lst_1:
    print("{:^15}".format(i), "{:^15}".format(lst_2.count(i)))
    i += 1

print("\n{:<15}" "{:<15}".format("Element list2", "Count in list1"))
for i in lst_2:
    print("{:^15}".format(i), "{:^15}".format(lst_1.count(i)))
    i += 1