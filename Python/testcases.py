import unittest 
import random 

class TestSequenceFunction(unittest.TestCase):
  def setUp(self):
    self.value = 1
    self.seq = [1,2,3]
    
  def test_notzero(self):
    self.assertNotEqual(self.value, 0)

  def test_in(self):
    self.assertIn(self.value, self.seq)

if __name__ == '__main__':
  unittest.main()
