import random
numbers = len(
    set([random.randint(-10, 10) for i in range(10)])
    |
    set([random.randint(-10, 10) for j in range(10)])
)
print(numbers)
