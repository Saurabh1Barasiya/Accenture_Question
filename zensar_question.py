# 25 77 54 81 48 34
# output - 2
# just check the square root of the number.

import math
n = int(input("Enter a number: "))
c= 0
nums = list(map(int, input("Enter a list of numbers: ").strip().split()))[:n] 
for i in nums:
    if len(str(math.sqrt(i))) <= 3:
        c = c+1
print(c)

