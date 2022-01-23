n = int(input("Enter a number: "))
nums = list(map(int, input("Enter a list of numbers: ").strip().split()))[:n] 
even = []
odd = []
for i in nums:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
for i in even+odd:
    print(i, end=" ")









