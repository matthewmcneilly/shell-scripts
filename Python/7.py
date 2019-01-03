import sys
import os

def fsize():
  #Print the filename 
  print("The filename is %s" % sys.argv[1])
  fsize = os.path.getsize('test.txt')
  print("The filesize is %s bytes in size" % fsize)


def fsize2():
  dval = None

  return dval  

fsize()
fsize2()
