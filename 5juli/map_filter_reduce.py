from functools import reduce

def up_name(name):
  return name.upper()

names = ['andy','benny','chika','dody']

proper_names = []

for name in names:
  proper_names.append(up_name(name))
  
print(proper_names)

print('Map')
proper_names = map(up_name, names)
print(list(proper_names))

print('Even Number')

def even_nums(numbers):
  even_list = []
  
  for num in numbers:
    if num % 2 == 0:
      even_list.append(num)
  
  print(even_list)
  
numbers = range(1,30)
even_nums(numbers)

print('Filter')
def is_even(number):
  return number % 2 == 0

even_numbers = filter(is_even, numbers)
print(list(even_numbers))

print('Reduce')

def addition(num1, num2):
  return num1 + num2

x = reduce(addition, numbers)
print(x)
