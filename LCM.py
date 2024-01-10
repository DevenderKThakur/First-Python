#  find the lcm of the number given 
# first method 
import math
def lcm(a,b):
    max_num = max(a,b)
    while True :
        if max_num  % a == 0 and max_num % b == 0:
            return max_num
        max_num += 1 
    return max_num

# print (lcm(4,6))

# second method 

def gcd (a,b):
    if a == 0 :
        return b 
    return gcd(b%a,a)

def lcm2(a,b):
    return (a*b) // (gcd(a,b))

print (lcm2(4,6))