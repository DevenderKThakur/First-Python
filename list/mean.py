# find the mean of the element in the list 
# fist method 
def mean_of_list (l):
    return sum(l)/len(l)


#  brute force approach 
def mean_of_list2(l):
    sum = 0 
    length_of_list = len(l)
    for item in l :
        sum += item 
    return sum / length_of_list    


l = [10,20,30,40]
print (mean_of_list2(l))

