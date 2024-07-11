today = "sunny"

if today == "sunny":
  print("i don't have use umbrella")
  print('text')
  
battery = "full"

if battery == "low":
  print('your battery is low')
  print('please, charger your battery...')
else:
  print('battery is full')
  

print('input your grade A/B/C')
grade = input().upper()

if grade == "A":
  print("Congratulation")
elif grade == "B":
  print("Good Job")
elif grade == "C":
  print("Good luck next time!")
else:
  print('wrong input')


score = 74

if score > 85 and score <= 100:
  print('grade A')
elif score > 70 and score <= 85:
  print('B')
else:
  print('C')
  
age = 18
driver_lisence = False

if age >= 17:
  print('user is teenager')
  if driver_lisence == True:
    print('And driving is allowed')
  else:
    print('But driving is not allowed')
else:
  print('user is not teenager')