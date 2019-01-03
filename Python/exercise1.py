# from __future__ import print_function


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = []

'''
### METHOD 1
for x in list1[0:-1:2]:
	list2.append(x)


print list2
'''

'''
# METHOD 2
list2.append(list1[0:-1:2])

print list2

'''

# Method 3 
list2 = list1[0:-1:2]
print list2



def make_second_one(inl):
	outl = []
	for i in xrange(1, len(inl), 2):
		outl.append(inl[i])
	return outl

def make_second_two(inl):
	outl = []
	for i in xrange(len(inl)):
		if i%2:
			outl.append(inl[i])
	return outl

def make_second_three(inl):
	return inl[1::2]





