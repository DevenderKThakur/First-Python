#  count the digits in the numbers 

 
def count(x):
    count_variable = 0
    while x > 0 :
        x = x//10
        count_variable += 1 
    return count_variable    
print (count(9583))