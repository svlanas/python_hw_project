def table(func):
    def table_set(n: object) -> object:
        set_ = list(func(n))
        set_.sort()
        for i in range(len(set_)):
            a = "кратне 3" if set_[i] % 3 == 0 else "не кратне 3"
            b = "парне" if set_[i] % 2 == 0 else "не парне"
            print(f'{set_[i]:>3} {a:<12} {b:<10}')

    return table_set


@table
def set_n(n: int) -> set:
    """

    :param n: number of set's elements
    :return: set with n elements
    """
    import random
    set_ = {random.randint(1, 100) for _ in range(n)}
    return set_


if __name__ == "__main__":
    set_n(5)
