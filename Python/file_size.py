import sys
import os

def main():
  #Print the filename
  fname = sys.argv[1] 
  print("The filename is %s" % fname)

  #Print the filesize 
  fsize = os.path.getsize(fname)  
  print("The filesize is %s bytes" % fsize)

  if fsize < 1024:
    return str(fsize) + ' bytes'
  elif 1024 < fsize < 1024*1024:
    return str(fsize/1024) + ' K'
  elif 1024*1024 < fsize < 1024*1024*1024:
    return str(fsize/(1024*1024)) + ' M'
  else:
    return str(fsize/(1024*1024*1024)) + ' G'  




print(main())

