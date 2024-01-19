# import random
# class Topi:
#     def __init__(self):
#         self.locations = ["Pathari", "Hasandaha", "Itahari", "Qatar"]

#     def sort(self, name):
#         print(name, "is in", random.choice (self.locations))


# topi = Topi()
# topi.sort("Sujan")

"""add more name"""
import random
class Topi:
    locations = ["Pathari", "Hasandaha", "Itahari", "Qatar"]
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice (cls.locations))

Topi.sort("Sujan")