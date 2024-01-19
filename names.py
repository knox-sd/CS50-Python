# save the input - file I/O

# name = input ("What's your name? ")
# print(f"Hello, {name}")

# names = []
# for _ in range(3):
#     name = input ("What's your name? ")
#     names.append(name)
#     print(f"Hello, {name}")


# names = []
# for _ in range(3):
#     names.append(input ("What's your name? "))
# for name in sorted(names):
#     print(f"Hello, {name}")

# open - store the data- save input

name = input("What's your name? ")
file = open("name.txt", "w")
file.write(name)
file.close()

