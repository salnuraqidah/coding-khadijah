import mymodule as mm
from random import randint
from mymodule import x
from mathematic.circle.area import area_of_circle
import hashlib as h

import math

print(mm.x)

mm.area_of_square(20)
mm.area_of_triangle(10,6)

print(x)

print(math.pi)
print(math.factorial(5))
print(math.sqrt(25))

area_of_circle(21)

# mypassword = '1234admin'
# encode_pass = mypassword.encode('utf-8')
# hashed_pass = h.sha256(mypassword).hexdigest()
# print(hashed_pass)