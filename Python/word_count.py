import sys

def rfile():
  fname = sys.argv[1]
  nbytes = 0
  nwords = 0 
  nlines = 0 
  words = None   
  lines = None

  gfile = file(fname, 'rb')
  fdata = gfile.read() 
  nbytes = len(fdata)
  words = fdata.split(' ')
  lines = fdata.split('\n')	  
  nwords = len(words)
  nlines = len(lines)  
 
  print 'The file is', nbytes, 'bytes in size'
  print 'The file has', nwords, 'words in it'
  print 'The file has', nlines, 'lines in it' 

rfile()
