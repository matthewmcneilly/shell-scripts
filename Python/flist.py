# Read in the file 
# Stick in it a list
# Output backout to the file 
# Use getitem and setitem 
# Create a class 


class FileList(object):
  def __init__(self, fname):
    self.fname = fname 

  def lfile(self):
    cfile = file('test.txt', 'r+')
    fdata = cfile.read()
    lsdata = list(fdata)
    for item in lsdata:
      cfile.write("%s\n" % item)


 
def main():


if __name__ == "__main__":
  main() 

