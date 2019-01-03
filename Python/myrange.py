def myrange(st, sp, stp):
  while st < sp:
    yield st 
    st+=stp

myrange(1, 6, 2)
