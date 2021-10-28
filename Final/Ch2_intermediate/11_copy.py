# Datatype must be mutable

# =
l1 = [1, 2, 3, 4]
l2 = l1
print(l1, l2)
l2[2] = 69
print(l1, l2)

# Shallow
l1 = [1, 2, 3, 4]
l2 = l1.copy()
print(l1, l2)
l2[2] = 69
print(l1, l2)

# shallow with nested
l3 = [[1, 2, 3, 4], [5, 6, 7, 8]]
l4 = l3.copy()

print(l3, l4)
print(l3[1][3])
l3[1][3] = 100

print(l3, l4)

l3.append([9, 10, 11, 12])
print(l3, l4)

# Deep
import copy
l5 = [1,2,3,4]
l6 = copy.deepcopy(l5)
l5[2] = 69
print(l5, l6)

l7 = [[1, 2, 3, 4], [5, 6, 7, 8]]
l8 = copy.deepcopy(l7)

print(l7[1][3])
l7[1][3] = 100

print(l7, l8)


# Memory address
