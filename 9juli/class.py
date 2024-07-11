class Animal:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def makeSound(self, sound):
    print(self.name, 'is making a', sound)
  
  def eat(self, food):
    print(f"{self.name} with {self.color} color is eating {food}")
  
cat = Animal("Kitty", "Black")
panda = Animal("Panda", "Black White")

cat.makeSound("miowing")
cat.eat("fish")

panda.makeSound('bleating')
panda.eat('bamboo')

print(type(cat))
print(type(panda))

