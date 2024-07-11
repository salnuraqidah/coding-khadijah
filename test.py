class Vehicle:
	def __init__(self, brand, model, color, maxSpeed):
		self.brand = brand
		self.model = model
		self.color = color
		self.maxSpeed = maxSpeed

	def start(self):
		msg = self.__class__.__name__.lower()+" starts the engine"
		return(msg)
	def stop(self):
		msg = self.__class__.__name__.lower()+" stops the engine"
		return(msg)
	def turn(self, direction):
		msg = self.__class__.__name__.lower()+" turns "+direction
		return(msg)

class Truck(Vehicle):
	def __init__(self, brand, model, color, maxSpeed, loadCapacity):
		super().__init__(brand, model, color, maxSpeed)
		self.loadCapacity = loadCapacity

	def load(self):
		msg = self.__class__.__name__.lower()+" loads goods to ship"
		return(msg)

object1 = Truck("Mitsubishi","Fuso FN 527 ML","Gray","76 kmph","24.800 Kg")

object2 = Vehicle("Mitsubishi","Fuso FN 527 ML","Gray","76 kmph")
print(object2.start())


msg1 = "This is "+object1.brand+" "+object1.model+" in "+object1.color
msg2 = "The maximum speed is "+object1.maxSpeed
msg3 = "And the maximum of load capacity is "+object1.loadCapacity

print(object1.start())
print("\n")
print(msg1)
print(msg2)
print(msg3)
print("\n")
print(object1.turn("right"))
print(object1.stop())