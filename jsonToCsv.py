import json

with open("input.json", "r") as file:
    data = json.loads(file.read())

output = ",".join([*data[0]])

for dictionary in data:
    output += f'\n{dictionary["Name"]},{dictionary["age"]},{dictionary["birthyear"]}'

with open("output.csv", "w") as file:
    file.write(output)