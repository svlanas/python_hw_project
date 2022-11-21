def sum_two_list_items(list_val, int_val):
    """
    function checks whether an integer is equal to
    the sum of any two list values
    :param list_val: list value
    :param int_val: integer value
    :return: True or False
    """
    list_val = list(list_val)
    int_val = int(int_val)
    # creating list of sums each two list values
    sum_list_items = []
    for i in range(len(list_val)):
        for j in range(len(list_val)):
            if i != j:
                sum_list_items.append(list_val[i] + list_val[j])
    # check is integer value in list of sums each two list values
    return int_val in sum_list_items


print(sum_two_list_items([1, 3, 8], 3))
print(sum_two_list_items([i for i in range(15)], 5))