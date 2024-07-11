def average_number(*numbers): # arbitraty argument
  result = 0 
  for num in numbers:
    result += num
  n = len(numbers)
  avg = result/n
  return avg

add1 = average_number(1,2,4,5,6,7,8,9,0,4,5,8,4,10,11,12)
print(add1)

avg1 = average_number(1,2,3,4,5,6,7,8,9,10)
print(avg1)