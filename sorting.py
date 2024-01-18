def bubbleSort(arr):
    swapped = False
    for item in range(len(arr)):
        for element in range(0,len(arr)-item-1):
            if arr[element] > arr[element+1]:
                swapped = True 
                arr[element] , arr[element+1] = arr[element+1] , arr[element]
        if not swapped:
            return 


arr = [12,3,4,5,6,13]

bubbleSort(arr)

print (arr)