def plus1(x):
  return x+1  

def make_log(func):
  def wrapper(*args, **kwargs):
    print('Called {}'.format(func.__name__))
    result = func(*args, **kwargs)
    print('Returning {}'.format(result))
    return result

  return wrapper

log_plus1 = make_log(plus1)


log_plus1(10)

