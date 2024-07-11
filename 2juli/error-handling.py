student = {
  "name" : "Alhazen",
  "address" : "Jakarta"
}

try:
  print(studen)
except NameError:
  print('name is not defined')
except:
  print('An error occured')
else:
  print('code success')
finally:
  print('done')
  
number1 = 10
number2 = 0

try:
  if number2 == 0:
    raise ZeroDivisionError("Error: cannot devide by zero")
  result = number1/number2
  print(result)
except ZeroDivisionError as e:
  print(e)
except ValueError:
  print('invalid input')