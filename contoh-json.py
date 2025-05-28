import json


data = {
    "employees": [
        {
            "firstName": "John",
            "lastName" : "Doe"},
        {
            "firstName": "Anna",
            "lastName" : "Jones"},
        {
            "firstName": "Peter",
            "lastName" : "Jones"}
    ]
}


print (type(data))

with open ("data_file.json", "w") as file:
    json.dump (data, file)

print (json.dump(data))






















