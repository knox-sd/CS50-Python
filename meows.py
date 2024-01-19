# MEOWS = 3
# for _ in range(MEOWS):
#     print("Meows")

# class Cat: # conscent class
#     MEOWS = 3
#     def meow(Self):
#         for _ in range(Cat.MEOWS):
#             print("meow")

# cat = Cat()
# cat.meow()

## mypy - checking program before execution
# def meow(n: int):
#     for _ in range(n):
#         print("meow")

# number: int = int(input("Number: "))
# meow(number)

## return value int to str if there is any error on converting
# def meow(n: int) -> None:
#     for _ in range(n):
#         print("meow")

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows)

# def meow(n: int) -> str:
#     return "meow\n" * n

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")

"""docstrings - documentation"""

# def meow(n: int) -> str:
#     """
#     Meow n times.
#     :para n: Number of times to meow
#     :type n: int
#     :raise TyperError: if n is not an int
#     :return: A string of n meow, one per line
#     :rtype: str
#     """
#     return "meow\n" * n

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows, end="")

""" -n => controling from terminal line (command line)"""
# import sys

# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#     print("usage: meows.py")

"""argparse - """
# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("-n")
# args = parser.parse_args()

# for _ in range(int(args.n)):
#     print("Meow")

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help = "Number of times to meow", type = int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("Meow")
