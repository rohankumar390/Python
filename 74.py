from functools import lru_cache
a=input("Enter the number\n")
@lru_cache(maxsize=100)
def hi(k):

    for i in range(k):
        print(a)
    print("compiled")
    
hi(3)
print("hi 1")
hi(4)
print("hi completed 2")
hi(3)
print("hi completed 3")