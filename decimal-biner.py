n = 27

n_bin = bin(n)
print(n_bin)
print(n_bin.replace("0b",""))

n_decimal = int(n_bin, 2)
print(n_decimal)

print("Bitwise Operator")
a = 15
b = 14

and_operator = a & b
print(f"{a} & {b} = {and_operator}")

or_operator = a | b
print(f"{a} | {b} = {or_operator}")

xor_operator = a ^ b
print(f"{a} ^ {b} = {xor_operator}")