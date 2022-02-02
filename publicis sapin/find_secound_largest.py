# find secound largest number .

# firt way.
arr = [10,2,1,45,30,74,85,90,456]
print(sorted(arr,reverse=True)[1])

# second way.
arr.sort(reverse=True)
print(max(arr[1:len(arr)]))

# third way.
arr = [10,2,1,45,30,74,85,90,456]
arr.sort()
print(arr[-2])




# fourth way.
arr = [10,2,1,45,30,74,85,90,456]
max = 0
s_max = 0
for i in arr:
    s_max = max
    if i > max:
        max = i


print("maximim value",max)
print("secound maximum value",s_max)

