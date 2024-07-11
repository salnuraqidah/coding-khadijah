names = ["Ahmad", "Benny", "Jhon", "Putri"]

for name in names:
  print(name)
  
# php
# for i = 0; i < 10; i++ {
# }

for i in range(10):
  print(i)
  
print('range with interval')

for i in range(1,20,2): # start, end, step
  print(i)
  
number = 1

print('break statement')

while number <= 10:
  print(number)
  if number == 3:
    break
  number += 1

print('continue statement')
 
for i in range(1,10):
  if i == 3:
    continue
  print(i)
else:
  print("all number are printed")
  
for i in range(10):
  pass

fruits = ["Apple", "Banana", "Cherry"]
colors = ["Green", "Yellow", "Red"]

for color in colors:
  for fruit in fruits:
    print(f"{color} {fruit}")
    
    
  