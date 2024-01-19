# name = input("Name: ")
# house = input("House: ")
# print(f"{name} from {house}")

# def main():
#     name = input("Name: ")
#     house = input("House: ")
#     print(f"{name} from {house}")

# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")

# if __name__ == "__main__":
#     main()


# def main():
#     name, house = get_student()
#     print(f"{name} from {house}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return name, house


# if __name__ == "__main__":
#     main()

# def main():
#     student = get_student()
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return name, house

# if __name__ == "__main__":
#     main()

"""overwrite the data"""

# def main():
#     student = get_student()
#     if student[0] == "Hari":
#         student[1] = "India"
#     print(f"{student[0]} from {student[1]}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house]

# if __name__ == "__main__":
#     main()

"""using dictionary"""

# def main():
#     student = get_student()
#     print(f"{student['name']} from {student['house']}")

# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student

# if __name__ == "__main__":
#     main()


# def main():
#     student = get_student()
#     # if student[0] == "Hari":
#     #     student[1] = "India"
#     print(f"{student['name']} from {student['house']}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name": name, "house":house}
# if __name__ == "__main__":
#     main()


"""over write the data"""
# def main():
#     student = get_student()
#     if student["name"] == "Hari":
#         student["house"] = "India"
#     print(f"{student['name']} from {student['house']}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name": name, "house":house}
# if __name__ == "__main__":
#     main()

"""using classes"""

# class Student:
#     ...

# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")

# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student

# if __name__ == "__main__":
#     main()


# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house

# def main():
#     student = get_student()
#     # if student["name"] == "Hari":
#     #     student["house"] = "India"
#     print(f"{student.name} from {student.house}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     student = Student(name, house)
#     return student

# if __name__ == "__main__":
#     main()

"""return direct to class and use raise if there is any error"""

# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Nepal", "India", "Qatar"]:
#             raise ValueError("Invalid House")
#         self.name = name
#         self.house = house

# def main():
#     student = get_student()
#     # if student["name"] == "Hari":
#     #     student["house"] = "India"
#     print(f"{student.name} from {student.house}")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)


# if __name__ == "__main__":
#     main()

"""print the outout direct
Use __str__
"""

# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Nepal", "India", "Qatar"]:
#             raise ValueError("Invalid House")
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"

# def main():
#     student = get_student()
#     print(student)

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)


# if __name__ == "__main__":
#     main()

"""use forth attribute"""
# class Student:
#     def __init__(self, name, house, power):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Nepal", "India", "Qatar"]:
#             raise ValueError("Invalid House")
#         self.name = name
#         self.house = house
#         self.power = power

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     def power(self):
#         match self.power:
#             case "Fast":
#                 return "🚀"
#             case "Lazy":
#                 return "🛁"
#             case "Fight":
#                 return "🙉"
#             case "Go":
#                 return "🚘"
#             case _:
#                 return "/"

# def main():
#     student = get_student()
#     student.hosue = "Hasandaha-6, Santi chowk"
#     print("Super Power!!")
#     print(student.power())

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     power = input("Power: ")
#     return Student(name, house, power)


# if __name__ == "__main__":
#     main()

"""over write data"""
# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Nepal", "India", "Qatar"]:
#             raise ValueError("Invalid House")
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"

# def main():
#     student = get_student()
#     student.house = "Hasandaha-6, Pathari" # over written code
#     print(student)

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)


# if __name__ == "__main__":
#     main()

"""use properties"""


# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name")
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     @property
#     def house(self):
#         return self._house

#     @house.setter
#     def house(self, house):
#         if house not in ["Nepal", "India", "Qatar"]:
#             raise ValueError("Invalid House")
#         self._house = house


# def main():
#     student = get_student()
#     print(student)


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)


# if __name__ == "__main__":
#     main()

"""seprate, seprate error chacking using setter"""
# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, name):
#         if not name:
#             raise ValueError("Missing Name")
#         self._name = name

#     @property
#     def house(self):
#         return self._house

#     @house.setter
#     def house(self, house):
#         if house not in ["Nepal", "India", "Qatar"]:
#             raise ValueError("Invalid House")
#         self._house = house


# def main():
#     student = get_student()
#     print(student)


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)


# if __name__ == "__main__":
#     main()

# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, name):
#         if not name:
#             raise ValueError("Missing Name")
#         self._name = name

#     @property
#     def house(self):
#         return self._house

#     @house.setter
#     def house(self, house):
#         if house not in ["Nepal", "India", "Qatar"]:
#             raise ValueError("Invalid House")
#         self._house = house


# def main():
#     student = get_student()
#     student._house = "Hasandaha-6, Pathari"
#     print(student)


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)


# if __name__ == "__main__":
#     main()

"""clean using classmethord"""
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: " )
        return cls(name, house)

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()