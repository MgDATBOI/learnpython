import numpy
import numpy as np  # pip3 install numpy
# https://www.youtube.com/watch?v=QUT1VHiLmmI

z = numpy.zeros(10)
print(z)
print(z.shape)

z.shape = (2, 5)
print(z)

# much faster than list comp
print(np.linspace(1, 10000, 10000))  # 1 to 10 with 5 elems

np.random.seed(0)
print(np.random.randint(10, size=6))

# np.sin()
# sum, prod, mean, std, var, min, max, argmin (idx of min), argmax (idx of max)

z = np.array([x for x in range(10)])
print(z < 6)
print(z[z > 5])

# np.where(condition, true, false)
# np.where(photo > 100, 255, 0)

# __add__
# np.array -> matrix add, not concat
# int -> add int to each value

# np.array @ np.array = dot product

# np.array[:, :, 0].T  transpose(rotate)
# np.sort(np.array)
