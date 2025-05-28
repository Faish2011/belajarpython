import json

json_string = """
    {
        "firstname": "Fanny",
        "lastname" : "Lorenz",
        "city"     : "Kaffrine",
        "country"  : "Senegal",
        "countrycode" : "NO",
        "email": "Fanny.Lorenz667@gmail.com"
    }
"""
python_dict = json.loads (json_string)

print (type(python_dict))
print (python_dict['firstname'])
print (python_dict['lastname'])































