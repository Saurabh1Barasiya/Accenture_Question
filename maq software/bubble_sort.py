arr = [1,2,3,4,5,6]

i = 0
while i < len(arr):
    j = i+1
    swap = True
    while j < len(arr):
        if arr[i]>arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
            swap = False
        j += 1
    print("iteration ", i)
    if swap:
        break
    i += 1
print("after swap")
print(arr)

# worst case: O(n^2)
# best case: O(n)