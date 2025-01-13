student = {"name" : "Jaka", "address" : "Jakarta"}

car = {
    "model" : "truck",
    "brand" : "ford",
    "year"  : 2010
}
    
print (type(student))
print (student)

print (type(car))
print (car)

print (student.keys())

print (student ["name"])

print (car.keys())

print (car ["brand"])

car ["color"] = "red"
car ["price"] = 140000000
print (car)

car.pop ("model")
print (car)

car.popitem ( )
print (car)










