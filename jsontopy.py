import json

with open ("data_file.json", "r") as file:
    python_dict = json.load (file)

print (python_dict)
print (python_dict ['firstName'])
print (python_dict ['lastName'])







































