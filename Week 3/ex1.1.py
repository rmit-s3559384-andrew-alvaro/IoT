import json
import requests

data = [{
    "firstName": "Matthew",
    "age": 29
},
{
    "firstName": "Shekhar",
    "age": 99
}]

with open("ex1.1.json", "w") as file:
    json.dump(data, file, indent = 4)

del data

with open("ex1.1.json", "r") as file:
    data = json.load(file)

print(data)
print()

print(json.dumps(data, indent = 4))
print()

print(data[0]["firstName"])
print()
