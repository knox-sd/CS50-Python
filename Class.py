class Vault:
    def __init__(self, golds=0, silvers=0, irons=0):
        self.golds = golds
        self.silvers = silvers
        self.irons = irons
    def __str__(self):
        return f"{self.golds} Gold, {self.silvers} Silver, {self.irons} Iron"
suja = Vault(100, 50, 25)
print(suja)