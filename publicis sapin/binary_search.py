def binary_search(arr,key):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid  = (low + high)//2
        if arr[mid]==key:
            print(f"{key} found at {mid}")
            break
        elif key > arr[mid]:
            low = mid + 1
        elif key < arr[mid]:
            high = mid - 1
    else:
        print(f"{key} not found")
arr = [5,10,14,22,30,47,85,45,2]
arr.sort()

binary_search(arr,22)