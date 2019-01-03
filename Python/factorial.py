def factorial(n):
    if n <=  0:
        return 1        
    else:
        return n * factorial(n-1)

print(factorial(4))


def factorial2(n):
    result = 1
    for i in xrange(2, n + 1):
        result *= i
    return result 

print(factorial2(4))
