cars = ("Honda", "Volvo", "Hyundai", "Toyota")
print(cars)
print(type(cars))

print(cars[2])

# cars[1] = "Tesla" # Error: item tuple tidak bisa diubah
# print(cars)

print("Tuple Manipulation")
cars_list = list(cars)
print(cars_list)

cars_list.append("Tesla")
print(cars_list)

cars = tuple(cars_list)
print(cars)
print(type(cars))
