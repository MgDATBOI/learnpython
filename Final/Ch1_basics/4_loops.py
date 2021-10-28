# While loops

# while True:
#     pass
# while False:
#     pass

c = 10
while c > 0:
    print("Lmao")
    c -= 1

inp = None
while inp != "q":
    inp = input("Enter to continue, q to quit: ")

# For loops
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "11"]
for number in my_list:
    print(number)
    # print(number * 2)

for i in range(10):
    print(i)
for i in range(0, 10, -1):
    print(i)

# len()
for i in range(len(my_list)):
    print(my_list[i])

# enumerate()
l = list("qwertyuiopa")
for i, elem in enumerate(l):
    print(f"{i} | {elem}")

# zip()
for char, num in zip(l, my_list):
    print(f"{char} | {num}")
