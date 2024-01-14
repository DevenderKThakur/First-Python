def print_list (l):
    even_list = [item for item in l if item % 2 == 0] # this is a way to add the value in the list short way 
    odd_list = [item for item in l if item % 2 != 0]
    return even_list,odd_list

def small_number (l,x):
    return [element for element in l if element < x]


l = [1,2,3,4,5,6,7,8,9,10]
# x = 5 
# print(small_number(l,x))

def max_element (l):
    max = 0 
    for item in l :
        if max < item :
            max = item 
    return max

# print (max_element(l))

def second_largest_element(l):
    max = 0 
    second_max =  -1 
    for item in l :
        if max < item :
            second_max = max 
            max = item 
    return second_max

# print (second_largest_element(l))

l1 = [12]
def check_sorted(l):
    start = 0 
    end = len(l) - 1 
    return True if l[start] <= l[end] else False 

print (check_sorted(l1))
        
