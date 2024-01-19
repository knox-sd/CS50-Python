

students = [{"name": "Sujan", "house":"Nepal"},
    {"name": "Ram", "house":"Nepal"},
    {"name": "Jitu", "house":"Nepal"},
    {"name": "John", "house":"Qatar"},
    {"name": "David", "house":"UK"}
    
]

houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)


"""add new set"""

# students = [{"name": "Sujan", "house":"Nepal"},
#     {"name": "Ram", "house":"Nepal"},
#     {"name": "Jitu", "house":"Nepal"},
#     {"name": "John", "house":"Qatar"},
#     {"name": "David", "house":"UK"}
    
# ]

# houses = set()
# for student in students:
#     houses.add(student["house"])

# for house in sorted(houses):
#     print(house)