#  seprate the even  and odd elements in the list 

def even_list (l):
    even_list_container = []
    for item in l :
        if item % 2 == 0 :
            even_list_container.append(item)
    return even_list_container

def odd_list (l):
    odd_list_container = []
    for item in l :
        if item % 2 != 0 :
            odd_list_container.append(item)
    return odd_list_container

l = [10,41,30,15,80]

print (f"Even list {even_list(l)} and Odd List {odd_list(l)}")