# If, elif, else
condition = True
if condition:
    print("The condition was true")
else:
    print("The condition was false")

con1 = True
con2 = False
if con1 and con2:
    print("Both con1 and con2 are true")
elif con1 or con2:
    print("con1 or con2 was true")
else:
    print("neither con1 nor con2 was true")

if con1:
    if con2:
        print("con1 and con2")

# Switch (match) case -> python 3.10
# match val:
#     case c:
#         pass
#     case _:
#         print("default")

# Ternary  operators