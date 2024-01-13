n = int (input ("Enter the size of the elements : "))

my_list = list(map(int , input ("Enter the elements in the list").strip().split()))[:n] # take input in the list 

print (my_list)