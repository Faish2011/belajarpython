class person:
    def __init__ (self, name, age, hairColor):
        self.name = name 
        self.age = age
        self.hairColor = hairColor

    def eat (self):
        msg = str (self.name) + "can also eat"

        return (msg)


object1 = person ("Ahmad", 12, "brown")
print (object1.__class__.__name__, "its a parent class")
print (object1.name, "its an object created from a person class")
print (object1.eat ())






























