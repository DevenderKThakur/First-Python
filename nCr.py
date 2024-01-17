def nCr (n,r) :
    if n == 0 or r == 0 or n == r :
        return 1 
    return nCr(n-1,r-1) + nCr(n-1,r) 

# print (nCr(5,2))

# print array recursive 

def print_array(arr):
    if len(arr) == 0 :
        return 
    print(arr[0],end=" ")
    print_array(arr[1:])

arr = [1,2,3,4,5]
print(print_array(arr))