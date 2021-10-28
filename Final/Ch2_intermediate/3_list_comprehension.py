# basics

# newlist = [expression for item in iterable if condition == True]

l = [x for x in range(100)]
print(l)

# speed
import time

before = time.time()
for i in range(100000):
    l = [x for x in range(100)]
    # del l
after = time.time()
print(f"List comp.  {after - before}")

before2 = time.time()
for i in range(100000):
    l = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        38,
        39,
        40,
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        58,
        59,
        60,
        61,
        62,
        63,
        64,
        65,
        66,
        67,
        68,
        69,
        70,
        71,
        72,
        73,
        74,
        75,
        76,
        77,
        78,
        79,
        80,
        81,
        82,
        83,
        84,
        85,
        86,
        87,
        88,
        89,
        90,
        91,
        92,
        93,
        94,
        95,
        96,
        97,
        98,
        99,
    ]
    # del l
after2 = time.time()
print(f"Pre-defined {after2 - before2}")

print("".join([s if s != "." else "-" for s in str]))

# Problems
# https://gist.github.com/doughsay/cb50d9e4d344230ebc166255a202f81d

# solutions
# https://gist.github.com/the-rahulpatel/c7c010ef7a16dd4f2b09cbe6d582ec06




# nested for-loops
[(letter, num) for letter in "abcd" for num in range(4)]


# dict comp
names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]
# print zip(names, heros)

my_dict = {name: hero for name, hero in zip(names, heros)}
print(my_dict)


# set comp
nums = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
print({num for num in nums})
print(set([num for num in nums]))


[x for x in range(100)]
(x for x in range(100))
