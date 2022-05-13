# f=open("rohan.txt","w")
# a = f.write("Rohan Bhai You are right")
# print(a)
# f.close()

# f = open("harry2.txt", "a")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()

# f = open("rohan.txt", "r+")
# # print(f.read())
# f.write(" thank you")
f = open("harry.txt")
f.seek(11)
print(f.tell())
print(f.readline())
# print(f.tell())

print(f.readline())
# print(f.tell())
f.close()
  
