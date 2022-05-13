# for i in range(10):
#     print(i)

# element =[0,1,2,3,4,5,6,7,8,9]
# i=3
students = [
    {"name": "Rohan", "Grade": 56},
    {"name": "Akash", "Grade": 16},
    {"name": "harsh", "Grade": 96},
]
# for t in range(2,20,5):
#     print(t)

# for student in students:
#     name = student["name"]
#     Grade = student["Grade"]
#     print(name)
#     print(Grade)

#  Destructuring in syntx

#     currencies = 0.8, 1.2
#     usd, eur = currencies
# print(usd)
# print(eur)

friends = [("Rolf", 25), ("Anne", 87), ("BOB", 12)]

# for name,age in friends:
#     print(f"{name} is {age} years old")


# for friend in friends:
#     name,age=friend
#     name=friends[0]
#     age=friends[1]
#     print(f"{name} is {age} years old")

# print statement for printing strings
print("Harry is a programmer", end="**")

# Print statement with a literal
print(1+87)

# This will print "Harry is a programmer**88" on the screen


l1 = [5, 1, 6, 7, 3, 2, 4, 5, 3, "Rohan", "Jaaani", "Mohamad"]

for i in l1:
    # if type(i)==int and i>=6:
    if str(i).isnumeric() and i >= 6:
        print(i)
