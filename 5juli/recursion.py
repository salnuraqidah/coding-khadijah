def countdown(number):
  print(number)
  if number == 0:
    return
  else:
    countdown(number-1)

countdown(10)

def factorial(number):
  if number <= 1:
    return 1
  else:
    result = number * factorial(number-1)
    return result
  

fac_7 = factorial(7)
print(fac_7)

fac_5 = factorial(5)
print(fac_5)