#__name__ is pronounced dunder name 

# Always include the object keyword for object classes
# Use kls for a class methods 
class Pair(object):
  # Always include the self keyword 
  def __init__(self, a, b):
    self.a = a 
    self.b = b 
  
  # Repr and str are the same 
  def __repr__(self):
    return "Pair({0},{1})".format(self.a, self.b)

  def __str__(self):
    return "Pair<{0}, {1}>".format(self.a, self.b)
  
  def __len__(self):
    return "2"

  def as_tuple(self):
    """Return as a tuple."""
     
    return self.a, self.b

  def __add__(self, other):
    """Combine two Pairs by adding the respective contained values"""
    return Pair(self.a + other.a, self.b + other.b)


class Temperature(object):
  def __init__(self, celsius):
    self.internal_celsius = celsius
  
  @property
  def farenheit(self):
    print('calling farenheit property')
    return (celsius * 9.0/5.0) + 32
 
def main():
  p1 = Pair(10, 20)
  p2 = Pair(3, 4)
  print(p1)
  print(repr(p1))
  print('{}'.format(p1))
  print('{!r}'.format(p1))
  print(p1 + p2)






# means main is only run if main is ran as the main program
# main wouldnt be run if this file is imported 
if __name__ == "__main__":
  main() 



'''
Multiple inheritience isnt recommended but can be done
Not really required because of how flexible python is 
Use mixins instead in order to add extra functionality

'''
