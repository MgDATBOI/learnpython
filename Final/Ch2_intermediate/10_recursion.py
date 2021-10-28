# What is recursion
# def f1(x):
#     return f1(x + 1)
# f1(1)


# base case
def f1(x):
    if x >= 500:
        return x
    else:
        return f1(x + 1)


print(f1(501))

# factorial


def fact(x):
    f = 1
    while x > 0:
        f *= x
        x -= 1
    return f


print(fact(5))


def factorial(x):
    if x <= 1:
        return x
    else:
        return factorial(x - 1) * x


print(factorial(5))

# fib example


def i_fib(n):
    if n < 0:
        return None
    a, b = 0, 1
    for x in range(n):  # n-1 for position, n for index(0 based)
        a, b = b, a + b
    return a


print(i_fib(6))


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


# print(fib(100))

# caching
import time
import sys

sys.setrecursionlimit(15000)
d = {}


def c_fib(n):
    if n in d:  #d.keys()   # 0.0009925365447998047s
        return d[n]

    if n == 1 or n == 2:
        return 1
    elif n > 2:
        d[n] = c_fib(n - 1) + c_fib(n - 2)
        return d[n]


before = time.time()
print(c_fib(1000))
after = time.time()
print(after - before)  # 0.0014867782592773438s
