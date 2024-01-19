"""operator overloading"""

# class Vault:
#     def __init__(self, golds=0, silvers=0, irons=0):
#         self.golds = golds
#         self.silvers = silvers
#         self.irons = irons
#     def __str__(self):
#         return f"{self.golds} Gold, {self.silvers} Silvers, {self.irons} Irons"

# sujan = Vault(100, 50, 25)
# print(sujan)

# ram = Vault(25, 30, 100)
# print(ram)

# golds = sujan.golds + ram.golds
# silvers = ram.silvers + ram.silvers
# irons = sujan.irons + ram.irons

# total = Vault(golds, silvers, irons)
# total = sujan + ram # error
# print(total)

class Vault:
    def __init__(self, golds=0, silvers=0, irons=0):
        self.golds = golds
        self.silvers = silvers
        self.irons = irons
    def __str__(self):
        return f"{self.golds} Gold, {self.silvers} Silvers, {self.irons} Irons"
    
    def __add__(self, other): # overloading operation function
        golds = self.golds + other.golds
        silvers = self.silvers + other.silvers
        irons = self.irons + other.irons
        return Vault(golds, silvers, irons)

sujan = Vault(100, 50, 25)
print(sujan)

ram = Vault(25, 30, 100)
print(ram)

golds = sujan.golds + ram.golds
silvers = ram.silvers + ram.silvers
irons = sujan.irons + ram.irons

total = sujan + ram #overloading operation
print(total)

