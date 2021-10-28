# Arithmetic
a = 10
b = 20
print(a + b)
c = a + b
print(c)
print(c - b)

# switch two variables without a third temporary variable
a = 10
b = 20
a = a + b
b = a - b
a = a - b
print(a, b)

print(a * b)
print("a" * b)
c = 5
d = 3
print(c / d)
print(c // d)
print(c ** d)
print(c % d)

# Logical
print(a == b)
print(a != b)
print(a < 10)
print(a <= 10)
print(True and True)
print(True or True)
print(not True)
print(not (True or True))  # not True and not True

# Assignment operators
e = 10
e += 1
e -= 1
e *= 2
# /=
# //=
# **=
# %=

# Bitwise  https://en.wikipedia.org/wiki/Bitwise_operation
a = 32 >> 1
a = 32 << 1
# &
# |
# ^

# &=
# |=
# ^=
# >>=
# <<=
