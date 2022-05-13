# def hello():
#     """WHY I AM SO CUTE"""
# print(hello.__doc__)


num=input()
num2=input()
try:
    print("The sum of these two numbers is",
          int(num)+int(num2))
except Exception as e:
    print(e)
