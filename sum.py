# sum of n natural numbers 
# first to ues the sum of n natural numbers 
def sum (n):
    return (n*(n+1))//2

#  use recursion to print the sum of n natural numbers 
def sum2 (n):
    if n == 1 :
        return 1 
    return n + sum2(n-1)

# print (sum2(10))
# print (sum (10))

def sum3 (n):
    sum = 0
    for item in range(n+1):
        sum += item
    return sum 
print (sum3(10))