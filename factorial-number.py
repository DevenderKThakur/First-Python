#  to print the factorial of a number 

# first method is recursion 

def fact (n):
    if n == 0 :
        return 1 
    return n * fact(n-1)

# print (fact(5))

# second method is using loop 
n = 0 
factorial_number = 1 
if n == 0 :
    print (1)
for item in range(1, n+1):
    factorial_number *= item 
print (factorial_number)

