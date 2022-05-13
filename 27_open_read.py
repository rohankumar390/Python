f = open("rohan.txt","rt")
# print(f.readline())
# print(f.readlines())

# for line in f:
#     print(line,end="")
    
content = f.read()
# print(content)

content = f.read(34455)
print("2", content)

f.close()