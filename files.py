# 1 & 2
filename = "name.txt"
name_input = False
# times = 0
out_file = open(filename, "w")

while not name_input:
    name_code = str(input("What code of your name?(Enter -1 will stop)"))
    if name_code == "-1":
        name_input = True
    else:
        # times += 1
        out_file.write(f"Your name is {name_code}\n")

out_file.close()


# 3
filename = "numbers.txt"

in_file = open(filename, "r")

line1_number = int(in_file.readline())
line2_number = int(in_file.readline())

result = line1_number + line2_number
print(result)

in_file.close()


# 4
filename = "numbers.txt"

in_file = open(filename, "r")

total = in_file.read()
print(total)

in_file.close()
