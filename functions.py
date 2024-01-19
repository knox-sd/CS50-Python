# n = int(input("wha' n ?"))
# for i in range(n):
#     print("*" *i)


# def main():
#     n = int(input("wha' n ?"))
#     for i in range(n):
#         print("*" *i)

# if __name__ =="__main__":
#     main()


# def main():
#     n = int(input("wha' n ?"))
#     for i in range(n):
#         print(sheep(i))

# def sheep(n):
#     return "#" * n

# if __name__ =="__main__":
#     main()


# def main():
#     n = int(input("wha' n ?"))
#     for s in sheep(n):
#         print(s)

# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("#" *i)
#     return flock

# if __name__ =="__main__":
#     main()

#> Generator function - massive data or list (keyword - "yield")

def main():
    n = int(input("wha' n ?"))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range (n):
        yield "#" * i

if __name__ =="__main__":
    main()