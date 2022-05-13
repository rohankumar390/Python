#------------------------Map-----------------------



num=["2","4","7"]
# num=list(map(int,num))
# print(num)


# for i in range (len(num)):
#     num[i]=int(num[i])

# num[2]=num[2]+1
# print(num[2])

def sq(a):
    return a*a;

# num=[2,3,4,5,7,1]
# square=list(map(sq,num))
# print(square)

# num=[2,3,4,5,7,1]
# square=list(map(lambda x:x*x,num))
# print(square)

# def square(a):
#     return a*a

# def cube(a):
#     return a*a*a

# fun=[square,cube]
# num=[2,3,4,5,6,7,8,9,10]

# for i in range(5):
#     val=list(map(lambda x:x(i),fun))
#     print(val)


#-----------------------------Filter________________________

# list_1=[1,2,3,4,5,6,7,8,9,10]

# def is_greater_5(num):
#     return num>5

# grthr_than_5=list(filter(is_greater_5,list_1))
# print(grthr_than_5)


#-------------------------Reduce------------------------------
from functools import reduce

list_1=[1,2,3,4]  

num=reduce(lambda x,y:x*y,list_1)
# num=0
# for i in list_1:
#     num=num+i

print(num)