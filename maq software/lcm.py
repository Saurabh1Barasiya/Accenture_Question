# least common multiple
# 4     6
# 8     12
# 12    18
# 16    24  
# 20    30
# 24    36

# least common multiple == 12 

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
max_possibilities = num1*num2
for i in range(1,max_possibilities+1):
    if i%num1==0 and i%num2==0:
        print("LCM is:",i)
        break