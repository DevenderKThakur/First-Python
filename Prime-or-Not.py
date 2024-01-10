# find the number is prime or not 
#  O(n)
def check(n):
    if n == 1 :
        return False 
    for item in range (2 , n):
        if n % item == 0 :
            return False
    return True 

# print (check(1031))
# O(N^1/2)
def check2(n):
    if n == 1 :
        return False 
    i = 2 
    while i * i  <= n :
        if n % i == 0 :
            return False 
    return True 

# print (check(41))

# super-efficent 

def check3 (n):
    if n == 1 :
        return False
    if n == 2 or n == 3 :
        return True 
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5 
    while i * i <=n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6 
    return True 

print (check3(1031))