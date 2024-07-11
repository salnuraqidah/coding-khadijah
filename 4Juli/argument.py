def extra_addition(*numbers): # arbitraty argument
  result = 0 
  for num in numbers:
    result += num
  return result

add1 = extra_addition(1,2,4,5,6,7,8,9,0,4,5,8,4)
print(add1)

def fullname(fname, lname='Nasution'):
  nama_lengkap = f'Hai {fname} {lname}'
  print(nama_lengkap)
  
fullname('salamah','aqidah')
fullname(lname='Academy', fname='Alhzen')
fullname('Raditya')

def NamaLengkap(**fullname):
  result = fullname.values()
  print(" ".join(result))
  
NamaLengkap(
  fname = 'Nur',
  mname = 'Habibah',
  lname = 'Lubis'
)
