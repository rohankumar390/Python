car={
    "hello":"Uncle",
    "How are you":"people",
    "chacha":False
    }

# print(car)

# print(car["chacha"])

# x = car.get("chacha")

x = car.keys()
y=car.values()
print(x)
print(y)

car["year"] = 2020

print(x) #after the change

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})


mydict = thisdict.copy()
print(mydict)
