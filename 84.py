import json
a ={"name":"harry","salary":9000,"language":"Python"}  
# conversion to JSON done by dumps() function
b = json.dumps(a)
print(b) # printing the output



# load(): This method is used to load data from a JSON file into a python dictionary.
# Loads( ): This method is used to load data from a JSON variable into a python dictionary.
# dump(): This method is used to load data from the python dictionary to the JSON file.
# dumps(): This method is used to load data from the python dictionary to the JSON variable.



# -----------------------------------------------------------------------------------------------------


# What is pickling?
# Pickling is the process of serializing an object. Serializing means storing the object in the form of binary representation so it can be saved in our main memory. The object could be of any type. It could be a string, tuple, or any other sort of object that Python supports. The data is stored in the main memory in a file. While writing the code for pickling, we open the file in "wb" mode, also known as writing binary mode. So, to use the pickle module, we have to make a file with the .pkl extension and send it in a dump() function along with the object. dump() is a built-in function in the Pickle module, made for pickling.



#
# 
# What is unpickling?
# The file format is binary, so we cannot directly open and read it; instead, we have to open it using a python program, and the process is known as unpickling. We have to open the file in "rb" mode for unpickling, also known as a read binary mode. The function we use this time is also a built-in function, named load(). Unlike dump(), we have to send the file name as a parameter, and it automatically retrieves the data in the object type it was inserted in. For example, if we send a list while pickling, the return result will also be a list.#



import pickle

# Pickling a python object
# cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))


# pickle.loads = ?




