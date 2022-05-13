list1=["Rohan","Akash","Fateh"]
list2={"Rohan":"Monitor","Akash":"President","Fateh":"VC"}
def fun(*args,**kargs):
    # for item in kargs:
    #     print(item)
    for key,value in kargs.items():
         print(f"{key} is a {value}")
fun(*list1,**list2)