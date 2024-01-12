# reverse a list 
l = [1,2,3,4,5]

def reverse1(l):
    rev = list(reversed(l))
    return rev 

# print (reverse1(l))

def reverse2(l):
    rev = l[::-1]
    return rev 

# print (reverse2(l))

def reverse3(l):
    start = 0 
    end = len(l) - 1 
    while start <= end :
        l[start] , l[end] = l[end] , l[start]
        start += 1 
        end -= 1 
    print (l)

reverse3(l)


