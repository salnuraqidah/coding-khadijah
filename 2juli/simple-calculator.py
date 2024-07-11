def addition(num1, num2):
  return num1+num2

def sub(num1, num2):
  return num1-num2

def multiply(num1, num2):
  return num1*num2

def div(num1, num2):
  try:
    result = num1 / num2
    return result
  except ZeroDivisionError:
    return "Error: Cannot divide by zero"

try:
  angka1 = float(input("Enter the first number: "))
  angka2 = float(input("Enter the second number: "))

  print("Addition: ", addition(angka1, angka2))
  print("Substaction: ", sub(angka1, angka2))
  print("Multiplication: ", multiply(angka1, angka2))
  print("Division: ", div(angka1, angka2))

except Exception as e:
  print(e)
  print("Error: Please enter valid number only")