import os

def rfile():
    # open the file
    test_file = file('test.txt', 'rb')
    # read the file
    data = test_file.read()

    # count find print filesize
    filesize = len(data)
    print 'The filesize is', filesize, 'bytes'

    filesize2 = os.path.getsize('test.txt')
    print filesize2    

    # close the file
    test_file.close()

rfile()
