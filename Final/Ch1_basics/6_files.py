# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exist

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

# "r+", "a+" - Read and write to the file: r: cursor at beginning of file, a: end of fileone

my_file = open("a.txt", "r")
for line in my_file:
    print(line)

print(my_file.read())

my_file.close()


with open("a.txt", "r") as f:
    lines = f.readlines()
# no need for close()

print(lines)  # -> list


