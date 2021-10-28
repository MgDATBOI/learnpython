# indexing
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(l[0])

# slicing
print(l[:])
print(l[1:4])
print(l[::-1])

###
# builtins
###
s = "qwertyuiop"
# string.split()
chars = s.split("t")
print(chars)
# string.join()
print(" ".join(chars))

# .replace()
s = s.replace("q", "Q")
print(s)

# .count()
print(s.count("w"))

# .upper()
print(s.upper())

# .lower()
print(s.lower())

# .title()
print("abc".title())


# .pop(index)
removed = l.pop(0)
print(removed)

# .remove()
l.remove(10)
print(l)
