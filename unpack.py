"""asking full name and return frist name only"""
# first, last = input("What's your name? ").split(" ")
# print(f"Hello, {first}")

# def total(golds, silvers, irons):
#     return(golds * 17 + silvers) * 29 + irons

# print(total(100,50,25), "Irons")


# def total(golds, silvers, irons):
#     return(golds * 17 + silvers) * 29 + irons
# coins = [100, 50, 25]
# print(total(coins[0], coins[1], coins[2]), "Irons")



"""unpacking the return value(*)"""
# def total(golds, silvers, irons):
#     return(golds * 17 + silvers) * 29 + irons
# coins = [100, 50, 25]
# print(total(*coins), "Irons")

# def total(golds, silvers, irons):
#     return(golds * 17 + silvers) * 29 + irons

# print(total(golds = 100, silvers = 50, irons = 25), "Irons")

"""using dictonary (**)"""
# def total(golds, silvers, irons):
#     return(golds * 17 + silvers) * 29 + irons
# coins = {"golds": 100, "silvers": 50, "irons": 25}
# print(total(**coins), "Irons")

"""return value- position, can be add or remove argumanet"""
# def f(*args, **kwargs):
#     print("Positional: ", args)
#     print("Named: ", kwargs)

# f(100, 50, 25)

"""return name- position, can be add or remove argumanet"""
# def f(*args, **kwargs):
#     print("Named: ", kwargs)

# f(golds = 100, silvers = 50, irons = 25)
