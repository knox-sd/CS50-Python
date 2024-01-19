"""veriable outside of function balance """

# balance = 0

# def main():
#     print("Balance: ", balance)

# if __name__ == "__main__":
#     main()


# balance = 0 # Error UnboundLocal Error

# def main():
#     print("Balance: ", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance: ", balance)

# def deposit(n):
#     balance += n

# def withdraw(n):
#     balance -= n


# if __name__ == "__main__":
#     main()


# def main(): # Error
#     balance = 0
#     print("Balance: ", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance: ", balance)

# def deposit(n):
#     balance += n

# def withdraw(n):
#     balance -= n


# if __name__ == "__main__":
#     main()

"""to use globle function- we have to call globle veriable"""
# balance = 0

# def main():
#     print("Balance: ", balance)
#     deposit(100)
#     withdraw(50)
#     print("Balance: ", balance)

# def deposit(n):
#     global balance
#     balance += n

# def withdraw(n):
#     global balance
#     balance -= n

# if __name__ == "__main__":
#     main()


"""new version for same program with deposit & withdraw"""

class Account:
    def __init__(self):
        self._balance = 0
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n
    
    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance: ", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance: ", account.balance)

if __name__ == "__main__":
    main()