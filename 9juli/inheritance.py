class Person:
  def __init__(self, name):
    self.name = name
    
  def getInfo(self):
    print(f"Hello {self.name}")
    
class Student(Person):
  def __init__(self, name, nis):
    super().__init__(name)
    self.nis = nis
    
  def study(self, subject):
    print(self.name, "is studying", subject)
  
  def getInfo(self):
    print(f"{self.name} NIS: {self.nis}")

person1 = Person('Amy')
person1.getInfo()

student1 = Student('Ahmad', '20240101')
student1.getInfo()
student1.study('math')