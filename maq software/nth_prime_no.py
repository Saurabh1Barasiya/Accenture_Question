n = int(input("Enter number : "))
k = n*100  
count = 0
for num in range(2, k):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        count += 1
    if count == n:
        print(num)
        break
