
import json

data = '{"var1":"harry", "var2":56}'

print(type(data))
print(data)

parsed = json.loads(data)
print(type(parsed))

#Task 1 - json.load?

# json.load() accepts file object.
# ex:
# with open("json_data.json", "r") as content:
#   print(json.load(content))

data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}

jscomp = json.dumps(data2)
print(jscomp)

# Task 2 = what is sort_keys parameter in dumps


# We use sort_keys parameter in json.dumps to specify if the result should be sorted or not. To specify that the result should be sorted we have to write this:
# import json
# data2 = {"Python" : "Awesome_programming_language","Coding" : "Awesome_skill"}
# jscomp = json.dumps(data2,sort_keys=True)

# print(jscomp)

# # The result will be this:
# {"Coding": "Awesome_skill", "Python": "Awesome_programming_language"}
# # As you can see the result is sorted