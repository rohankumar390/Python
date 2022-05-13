a="Hello"
# print(a[0])

# for x in a:
#     print(x,end=" ")
#     print(len(a))

# print("e" in a)

b="hello World"

# print(b[2:5])

print(b[:4])

print(b[2:])

print(b[-5:-2])

print(b.strip())

print(b.split(","))


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))