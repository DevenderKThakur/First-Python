#  to tell that a number is palindrome or not 

def palindrome_or_not(n):
    temp = n 
    rev = 0
    while temp != 0:
        rev = (rev * 10) + (temp % 10)
        temp = temp // 10 
    return rev == n 

print (palindrome_or_not(151))
