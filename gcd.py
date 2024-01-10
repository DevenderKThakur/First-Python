# find the greatest common divisor 

#  take two input and find the greatest common divisor 

import math 

# first method 

def gcd (a,b):
    for item in range(2,a):
        if a % item == 0 and b % item == 0:
            return item 

# print(gcd(4,6)
        
# Euclid Algorithm            
def gcd2(a,b):
    while a != b :
        if a > b :
            a = a - b 
        else :
            b = b - a 
    return a # here return a or b 

# print (gcd2(12,15))

# Recursion 

def gcd3(a,b):
    if a == 0:
        return b 
    return gcd3(b%a,a)

print (gcd3(12,15))


