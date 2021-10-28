# Try except finally
try:
    f = open("DNE.txt", "r")
    f.readlines()
except FileNotFoundError:
    pass
finally:
    f.close()

# different errors

try:
    pass
except Exception as e:
    if isinstance(e, ValueError):
        pass

