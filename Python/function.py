def mysum(a, b=0, *args, **kwargs):
  result = a + b 
  for i in xrange(len(args)):
    result += args[i]
  for k in kwargs:
    result += kwargs[k]
  return result


params = (10, 5, 5, 10)
dparams = {'one': 100, 'two': 200}
mysum(2, 3)
mysum(*params)
mysum(10, **dparams)
mysum(2, 3, 4, 5, 6, 7, more=100, values=200)
