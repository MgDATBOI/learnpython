# Basics
my_array = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
]

print(my_array[4])
print(my_array[4][1])

my_array2 = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
]


def add_2d_arr(arr1, arr2):
    new_arr = []
    for (
        row1,
        row2,
    ) in zip(arr1, arr2):
        new_row = []
        for num1, num2 in zip(row1, row2):
            new_row.append(num1 + num2)
        new_arr.append(new_row)
    return new_arr


my_arr3 = add_2d_arr(my_array, my_array2)

[print(line) for line in my_arr3]

# list comp
my_2d_array = [x for x in range(10)]
[print(line) for line in my_2d_array]

my_2d_array = [[x for x in range(10)]]
[print(line) for line in my_2d_array]

my_2d_array = [[i for i in range(10)] for j in range(10)]
[print(line) for line in my_2d_array]

print()

my_2d_array = [[int(i) for i in list("0" * 10)] for j in range(10)]
[print(line) for line in my_2d_array]

print()

import random

my_2d_array = [[random.randint(0, 9) for x in range(10)] for j in range(10)]
[print(line) for line in my_2d_array]

# Usecases
# game maps
# ascii art
# 

# operations
# all matrix operations

# https://en.wikipedia.org/wiki/Matrix_(mathematics)

# Expansion
# * operator, not 2*3 = 6, but *list

# 1-liner rotation
# rotated = zip(*original[::-1])  # https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
