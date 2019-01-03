

def double(tup1, tup2):
  for i in tup1:
    yield i 

  for i in tup2:
    yield i

for i in double((10, 12), (-1, -2, -5)):
  print(i) 

 
