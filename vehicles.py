class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Example usage:
vehicles = [Car(), Plane()]
for v in vehicles:
    v.move()