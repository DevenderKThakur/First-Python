def power(x,n):
    return x ** n 

# print (power(2,3))

def power2(x,n):
    pow = 1 
    for item in range (n):
        pow = pow * x 
    return pow 

# print(power2(7,2))

def power3 (x,n):
    if n == 0:
        return 1 
    if x == 0 :
        return 0 
    return x * power3(x,n-1)

print(power3(12,5))
# y = 5
# x = True if int (y/2) and y // 2 else False  
# print (x)
# divide and Conquer O(logn)
def power4 (x,n):
    if n == 0 :
        return 1 
    if x == 0 :
        return 0 
    temp = power4(x,n//2)
    if n % 2 == 0  :
        return temp * temp 
    else :
        return temp * temp * x 
    
print (power4(12,5))
  
