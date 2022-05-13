from ast import Delete
import calendar
import cmath
import random

# num1 =input("Enter first number\n")
# num2=input("Enter two number\n")

# sum=float(num1)+float(num2)

# print(sum,end="\n")

# print('The sum of {0} and {1} is {2}'.format(num1,num2,sum))


# # Store input numbers:
# num1 = input('Enter first number: ')
# num2 = input('Enter second number: ')

# # Add two numbers
# sum = float(num1) + float(num2)
# # Subtract two numbers
# min = float(num1) - float(num2)
# # Multiply two numbers
# mul = float(num1) * float(num2)
# #Divide two numbers
# div = float(num1) / float(num2)
# # Display the sum
# print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# a=float(input('Enter a: '))
# b=float(input('Enter b: '))
# c=float(input('Enter c: '))

# d=(b**2)-(4*a*c)

# sol1=(-b-cmath.sqrt(d))/(2*a)

# sol2=(-b+cmath.sqrt(d))/(2*a)

# print('The solution are {0} and {1}'.format(sol1,sol2))

# P=5;
# Q=4

# P,Q=Q,P
# # print(P,Q)

# n=random.random()

# print(n)


# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
# print(calendar.month(yy,mm))


# num=int(input("Enter a number: "))
# if(num %2) == 0:
#     print("{0} is even number ".format(num))
# else:
#     print("{0} is odd number".format(num))


# arr1=[1,2,3,4,5]

# arr2=[None]*len(arr1)

# for i in range(0,len(arr1)):
#     arr2[i]=arr1[i]

# print("Element of original array\n")

# for i in range(0,len(arr1)):
#     print(arr2[i]),

# list1=['h arry','ram','Akash',4,7]

# d1={}

# d2={
#     "Harry":"Burger",
#     "Rohan":"Fish",
#     "SkillF":"Roti",
#     "Shubam":{"B":"maggie","L":"roti"}
# }
# d2["Ankit"]="Junk Food"
# d2[420]="Kebab"
# # print(d2)
# del d2[420]
# # print(d2)
# d3=d2.copy()
# print(d3)
# d2.update({"Leena":"Toffee"})
# print(d2)


# s=set()
# print(type(s))
# l=[1,2,3,4,5]
# s_from_list=set(l)
# print(s_from_list)
# s.add(1)
# s.add(2)
# s1={4,6}
# print(s.isdisjoint(s1))


# dict1={
#     "Best Python course":"CodeWithharry",
#     "Best C languge course":"CodeWithHarry",
#     "Harry Sir":"Tom cruise of programming"
# }

# for x,y in dict1.items():
#     print(x,y)

# items=[int,float,"HaErry",4,7,2,1]

# for item in items:
#     if str(item).isnumeric() and item>=6:
#         print(item)


# i=0
# while(True):
#     print(f"The value of i is: {i}")
#     i=i+1
#     if(i>10):
#         print("Breaking the loop. ")
#         break


# a=330
# b=212

# print("EQUAL") if a==b else print("NOT EQUAL")

print("Enter num1\n")
num1 = input()
print("Enter num2\n")
num2 = input()
try:
    print("The sum of these two numbers is", int(num1)+int(num2))
except Exception as e:
    print(e)

print("This line is very important")