x = "global"

def foo():
  print(x)

print('luar fungsi', x)  
foo()

def test_local_scope():
  y = "text local scope"
  print(y)

test_local_scope()
# print(y) # error: not defined

score = 0
point = 0
name = 'Ahmad'

def tambah_score():
  global score, point
  score = score + 1
  point += 10
  name = 'Alhazen'
  print(score)
  print('point',point)
  print(name)
  
tambah_score()
tambah_score()
tambah_score()
print(name)