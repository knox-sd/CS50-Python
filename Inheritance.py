"""Inheritance"""

# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name")
#         self.name = name
#         self.house = house


#     ...

# class Professor:
#     def __init__(self, name, subject):
#         if not name:
#             raise ValueError("Missing name")
#         self.name = name
#         self.subject = subject
#     ...

"""add comman function or attribute in seprate class to use requried function"""

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house


    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    ...

Wizard = Wizard("Book")
student = Student("Sujan", "Hasanda")
Professor = Professor("David", "UK")