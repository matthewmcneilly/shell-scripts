import random
import time 

# generate random number
rnum = random.randrange(0, 0xffffffff)
# fetch time 
t = int(time.time()) 

hrnum = hex(rnum)
ht = hex(t)

