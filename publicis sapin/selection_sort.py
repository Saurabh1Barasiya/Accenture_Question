# selectin sort algorithm.

arr = [5,4,12,78,1,1,0,20]
i=0
while i<len(arr)-1: 
    j = i+1
    while j<len(arr):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        j = j+1
    print(f"{arr} and {i}")
    i = i+1
print("After sorting: ", arr)