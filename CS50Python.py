# x = int(input("X value? "))
# y = int(input("Y value? "))
# if x < y or x > y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")


# x = int(input("X value? "))
# y = int(input("Y value? "))
# if x != y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")


# x = int(input("X value? "))
# y = int(input("Y value? "))
# if x == y:
#     print("x is equal to y")
# else:
#     print("x is not equal to y")

#and operator
# score = int(input("Score: "))

# if score >= 90 and score <= 100:
#     print("Grade : A")
# elif score >= 80 and score < 90:
#     print("Grade : B")
# elif score >= 70 and score < 80:
#     print("Grade : C")
# elif score >= 60 and score < 70:
#     print("Grade : D")    
# else:
#     print("Grade : F")

# score = int(input("Score: "))

# if 90 <= score <= 100:
#     print("Grade : A")
# elif 80 <= score < 90:
#     print("Grade : B")
# elif 70 <= score < 80:
#     print("Grade : C")
# elif 60 <= score < 70:
#     print("Grade : D")    
# else:
#     print("Grade : F")


# def main():
#     x = int(input("Enter x value: "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     return n % 2 == 0
# main()

#Match

# name = input("What is your name? ")
# if name == "Hary":
#     print("Gryffindor")
# elif name == "Sujan":
#     print("Qatar")
# elif name == "jitu":
#     print("Nepal")
# elif name == "Suman":
#     print("Nepal")
# else:
#     print("Who?")


# name = input("What is your name? ")
# if name == "Hary":
#     print("Gryffindor")
# elif name == "Sujan":
#     print("Qatar")
# elif name == "Jitu" or name == "Suman" or name == "Jitesh":
#     print("Nepal")
# else:
#     print("Who?")


# name = input("What is your name? ")
# match name:
#     case "Sujan":
#         print("Qatar")
#     case "Suman":
#         print("UAE")
#     case "Jitu":
#         print("Nepal")
#     case "Jitesh":
#         print("Nepal")
#     case _:
#         print("Who?")


# name = input("What is your name? ")
# match name:
#     case "Sujan" | "Ramji" | "John":
#         print("Qatar")
#     case "Suman":
#         print("UAE")
#     case "Jitu":
#         print("Nepal")
#     case _:
#         print("Who?")

## Loops ## While
# print("meow")
# print("meow")
# print("meow")

# i = 3
# while i != 0:
#     print("meow")
#     i -= 1 # i = i - 1

# i = 1
# while i <= 3:
#     print("meow")
#     i += 1 # i = i + 1

# i = 0
# while i < 3:
#     print("meow")
#     i += 1 # i = i + 1

## Loops ## for (List)
# for i in [0, 1, 2]:
#     print("meow")

# for i in range(5): #define function rang()
#     print("meow")

# for _ in range(5): # if the veriable not required just put _
#     print("meow")

# print("meow\n" * 3) #with new line
# print("meow\n" * 3, end = "") #remove line at last

#user define
# while True:
#     n = int(input("What's n? "))
#     if n < 0:
#         continue
#     else:
#         break
# for _ in range(n):
#     print("Meow")

# while True:
#     n = int(input("Enter the numebr? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("Meow")

#function
# def main():
#     meow(3)
    
# def meow(n):
#     for _ in range(n):
#         print("Meow")

# main()

# def main():
#     number = get_number()
#     meow(number)

# def get_number():
#     while True:
#         n = int(input("Enter the numebr? "))
#         if n > 0:
#             break
#     return n

# def meow(n):
#     for _ in range(n):
#         print("Meow")
# main()

#List []
# student = ["Hery", "Ron", "Shym"]
# print(student[0])
# print(student[1])
# print(student[2])

# students = ["Hery", "Ron", "Shym"]
# for students in students:
#     print(students)

# students = ["Hery", "Ron", "Shym"] # using conunt method
# for i in range(len(students)):
#     print(students[i])

# students = ["Hery", "Ron", "Shym"] # using count method
# for i in range(len(students)):
#     print(i, students[i])
# students = ["Hery", "Ron", "Shym"] # using count method
# for i in range(len(students)):
#     print(i + 1, students[i])

#Dictonary {}
# students = {"Hery": "USA",
#             "Harry": "UK",
#             "Sujan": "Nepal",
#             "Shym": "Nepal"
#             }
# print(students["Harry"])
# print(students["Hery"])
# print(students["Sujan"])
# print(students["Shym"])

# students = {"Hery": "USA",
#             "Harry": "UK",
#             "Sujan": "Nepal",
#             "Shym": "Nepal"
#             }
# for student in students:
#     print(student)

# students = {"Hery": "USA",
#             "Harry": "UK",
#             "Sujan": "Nepal",
#             "Shym": "Nepal"
#             }
# for student in students:
#     print(student, students[student])

# students = {"Hery": "USA",
#             "Harry": "UK",
#             "Sujan": "Nepal",
#             "Shym": "Nepal"
#             }
# for student in students:
#     print(student, students[student], sep = ", ")

# students = [
#     {"name": "Hery", "house": "USA", "Vachile" : "Bike"},
#     {"name": "Harry", "house": "UK", "Vachile" : "Car"},
#     {"name": "Shym", "house": "Nepal", "Vachile" : "Cycle"},
#     {"name": "Sujan", "house": "Nepal", "Vachile" : None} #if there is nothing
# ]
# for student in students:
#     print(student["name"], student["house"],student["Vachile"], sep=", ")

# Mario brick
# print("#")
# print("#")
# print("#")

# for _ in range(3):
#     print("#")

# def main():
#     print_column(3)
    
    
# def print_column(height):
#     for _ in range(height):
#         print("#")
# main()

# def main():
#     print_column(3)
# def print_column(height):
#     print("#\n" * height, end="")
# main()

#mario question mark brick

# def main():
#     print_row(4)
# def print_row(width):
#     print("?" * width)
# main()

# Mario squre box brick 3x3
# def main():
#     print_square(3)
# def print_square(size):
#     #For each row in square
#     for i in range(size):
        
#         #For each brick in row
#         for j in range(size):
            
#             #print brick
#             print("#", end="")
#         print()
# main()

# def main():
#     print_square(3)
# def print_square(size):
#     for i in range(size):
#         print("#" * size)
# main()

# def main():
#     print_square(3)
# def print_square(size):
#     for i in range(size):
#         print_row(size)
# def print_row(width):
#     print("#" * width)
# main()

# Exceptions
#print("Hello, world) " syntax error

# x = int(input("Enter x value: ")) #you can't type letter in integer
# print(f"x is {x}")

#try & except = if the literal goes wrong
# try:
#     x = int(input("Enter x value: "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")

# try: #name error 
#     x = int(input("Enter x value: ")) #right to left not define
# except ValueError:
#     print("x is not an integer")
# print(f"x is {x}")

# try: #name error #corret with else
#     x = int(input("Enter x value: ")) #right to left not define
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

# making loop for checking errors if you type wrong
# while True:
#     try:
#         x = int(input("Enter x value: ")) #right to left not define
#     except ValueError:
#         print("x is not an integer or num")
#     else:
#         break  #always use break using while for checking
# print(f"x is {x}")

# while True:
#     try:
#         x = int(input("Enter x value: ")) #right to left not define
#         break #using break 1st
#     except ValueError:
#         print("x is not an integer or num")
# print(f"x is {x}")

#using function
# def main():
#     x = get_int()
#     print(f"x is {x}")
# def get_int():
#     while True:
#         try:
#             x = int(input("Enter x value: "))
#         except ValueError:
#             print("x is not an integer or num")
#         else:
#             break
#     return x
# main()

#short version
# def main():
#     x = get_int()
#     print(f"x is {x}")
# def get_int():
#     while True:
#         try:
#             x = int(input("Enter x value: "))
#         except ValueError:
#             print("x is not an integer or num")
#         else:
#             return x
# main()

# def main():
#     x = get_int()
#     print(f"x is {x}")
# def get_int():
#     while True:
#         try:
#             x = int(input("Enter x value: "))
#             return x
#         except ValueError:
#             print("x is not an integer or num")
# main()

# def main():
#     x = get_int()
#     print(f"x is {x}")
# def get_int():
#     while True:
#         try:
#             return int(input("Enter x value: "))
#         except ValueError:
#             print("x is not an integer or num")
# main()

#if you found error show input without except value. "Pass"
# def main():
#     x = get_int()
#     print(f"x is {x}")
# def get_int():
#     while True:
#         try:
#             return int(input("Enter x value: "))
#         except ValueError:
#             pass
# main()

# def main():
#     x = get_int("What's x? ")
#     print(f"x is {x}")
# def get_int(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             pass
# main()

#raise
#video 7 Debugging
#WAP to print pyramid
#
##
###
# def main():
#     height = int(input("Height: "))
#     pyramid(height)
# def pyramid(n):
#     for i in range(n):
#         print("#" * i)
# if __name__ == "__main__":
#     main()

# def main():
#     height = int(input("Height: "))
#     pyramid(height)
# def pyramid(n):
#     for i in range(n):
#         print("#" * (i + 1))
# if __name__ == "__main__":
#     main()

#breakpoints - what line do you wan a break (pause) click in number read dot .

# def main():
#     height = int(input("Height: "))
#     pyramid(height)
# def pyramid(n):
#     for i in range(n):
#         print("#" * (i+1))
# if __name__ == "__main__":
#     main()

# Libraries - share code with you for reuse the code from old to new

#random - by defult (random.py)
# to use libraries function start from import

# random.choice(seq) "All fo the choice"

# generate a random numebr

# import random

# coin = random.choice(["heads", "tails"])
# print(coin)

#from - select only choice case (to make short code)

# from random import choice

# coin = choice(["heads", "tails"])
# print(coin)

# random.randint(a, b) generate number from 1 to 10

# import random
# number = random.randint(1, 10)
# print(number)

#random.shuffle(x) - shuffle from list or cards
# import random
# cards = ["Jack", "Queen", "King"]

# random.shuffle(cards)
# # print(cards)
# for card in cards:
#     print(card)

# statistics - avg, min, max, sum
# import statistics
# print(statistics.mean([100, 90]))

# pasing argument

#sys.veriable (sys.argv) argument victor

# import sys
# 
# print("Hello, my name is", sys.argv[1])


# import sys
# try:
#     print("Hello, my name is", sys.argv[1])
# # print("Hello, my name is", sys.argv[0])
# except IndexError:
#     print("Too few arguments")

#for frist name & for 1st and 2nd name use "Sujan Ad"
# import sys

# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("Hello, my name is", sys.argv[1])

# import sys # list index error

# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")

# # print name tags
# print("Hello, my name is", sys.argv[1])

# import sys # list index error solution

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# print("Hello, my name is", sys.argv[1])

# import sys # short version print 3 name

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# for arg in sys.argv:
#     print("Hello, my name is", arg) #print 4 line including question
#solution
# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# for arg in sys.argv[1:]: #slices [1: -1] reverse 
#     print("Hello, my name is", arg)

# packages - third party Libraries - PyPI (python packages index)
# to install 3rd party packages using pip (to package manager)
# cowsay - cowsay something in screen
# goto the terminal & type pip install cowsay

# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.cow("hello, " + sys.argv[1])
#     cowsay.trex("hello, " + sys.argv[1])

# APIs - use other API program in python using requests Libraries
# pip install requests
# import requests
# import sys
# if len(sys.argv) != 2:
#     sys.exit()

# requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer=" + sys.argv[1])

# print(respone.json()) - to summrize data

# import json
# import requests
# import sys
# if len(sys.argv) != 2:
#     sys.exit()

# requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer=" + sys.argv[1])

# print(json.dumps(response.json(), indent=2))

# to open track records
# import json
# import requests
# import sys
# if len(sys.argv) != 2:
#     sys.exit()

# requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=weezer=" + sys.argv[1])

# print(json.dumps(response.json(), indent=2))

# o = response.json()
# for result in o ["results"]:
#     print(result["trackName"])

"""
9 Style
PEP 8 (Pythone Enchance Program) - style guide " Readability counts"
1. Indentation
2. Taba or Spaces?
3. Blank Lines
4. Imports
5. ...

There is defult tools "pyline" to install pip install pylint
pyline
pycodestyle
blank - shortout <arrange in format> auto format
"""
# #10 Unit Tests - Testing of program
# def main():
#     x = int(input("what's x: "))
#     print ("x squared is", square(x))

# def square(n):
#     return n*n
# if __name__ == "__name__": # crocess check from
#     main()