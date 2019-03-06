def div(num1, num2):
    return num1 / num2 

def sortlist(lst):
    alist = lst[:] # a slice (creates a copy)
    print(alist)
    for passnum in range(len(alist)-1, 0, -1):
        print(passnum)
        for i in range(passnum):
            if alist[i] < alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist 


