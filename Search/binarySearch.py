def binarySearchMain(arr,target):
    return binarySearch(arr,target,0,len(arr)-1)

def binarySearch(arr,target,start,end):
    if start > end :
        return -1
    mid = start + (end - start)//2 
    if arr[mid] == target :
        return mid 
    elif arr[mid] < target :
        return binarySearch(arr,target,mid+1,end)
    else:
        return binarySearch(arr,target,start,mid-1)
    


arr = [1,2,3,4,5,6]

target = 3 

print (binarySearchMain(arr,target))