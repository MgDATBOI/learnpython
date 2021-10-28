# what are lambda functions and how do you write one

# 3x +1
def f(x):
    return (3 * x) + 1


print(f(7))

lambda x: 3 * x + 1
g = lambda x: 3 * x + 1
print(g(7))

print((lambda x: 3 * x + 1)(7))


# Combine first+last name
def full_name(fn, ln):
    return f"{fn.strip().title()} {ln.strip().title()}"


print(full_name("Joe", "Brown"))

full_name = lambda fn, ln: f"{fn.strip().title()} {ln.strip().title()}"
print(full_name("JoE   ", "Brown "))


# Pattern
# lambda arg1, arg2, arg3: return
# lambda [arg]: <return>

names = [
    "Janet Parsons",
    "Vaughn Lewis",
    "Adonis Julius Archer",
    "Shelby Nathan Yoder",
    "Marin Alvarez",
    "London Lindsey",
    "Beau Tristan Bentley",
    "Leo Gardner",
    "Hunter Uriah Mathew Clarke",
    "Mikayla Lopez",
    "Frankie Conner Ritter",
]
names.sort(key=lambda name: name.split(" ")[-1].lower())
[print(name) for name in names]

nums = [x for x in range(10)]
nums_sqrd = list(map(lambda x: x ** 2, nums))
print(nums_sqrd)
