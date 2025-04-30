class vehicle:
    def __init__ (self, brand, model, color, maxSpeed):
        self.brand = brand
        self.model = model
        self.color = color
        self.maxSpeed = maxSpeed

    def start (self):
        return f"the {self.brand} {self.model} is starting"
    def stop (self):
        return f"the {self.brand} {self.model} is stopping"
    def turn (self, direction):
        return f"the {self.brand} {self.model} is turning {direction}"

class truck (vehicle):
    def __init__(self, brand, model, color, maxSpeed, loadCapacity):
        
        super (). __init__(brand, model, color, maxSpeed)
        self.loadCapacity = loadCapacity
    def load (self, weight):
        if weight <= self.loadCapacity:
            return f"loading {weight}kg into the truck"
        else: 
            return f"cannot load {weight}kg, exceeds the load capacity of {self.loadCapacity}kg"

my_truck = truck ("ford", "f-150", "red", 120, 1000)

print (f"truck brand: {my_truck.brand}")
print (f"truck model: {my_truck.model}")
print (f"truck color: {my_truck.color}")
print (f"truck max speed: {my_truck.maxSpeed} km/h")
print (f"truck load capacity: {my_truck.loadCapacity} kg")


print (my_truck.start ())
print (my_truck.stop ())
print (my_truck.turn ("left"))
print (my_truck.load (800))
print (my_truck.load (1200))






















