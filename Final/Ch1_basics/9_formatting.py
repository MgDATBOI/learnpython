var = "lmao"

# f""
print(f"lmao {var} lmao")

# .format()
print("lmao {} lmao".format(var))

# % formatting
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes

print("lmao %s lmao" % var)

# :formatting

n = 100000

print(f"{n:,}")

n = 1654783965783

print(" " * 20)
print(f"---{n:F}---")

# https://docs.python.org/3/library/string.html#formatstrings