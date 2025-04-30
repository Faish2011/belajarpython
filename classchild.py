class person: 
    def __init__(self, name, age, haircolor):
        self.name = name
        self.age = age
        self.haircolor = haircolor
    def eat (self):
        msg = str (self.name) + " can also eat"
        return (msg)
    def drink (self):
        msg = str (self.name) + " can also drink"
        return (msg)


class student (person):
    pass


object1 = student ("Ahmad", 10, "dark")
classname = object1.__class__.__name__

print ("object", object1.name, "is made of", classname)
print (object1.eat ())























