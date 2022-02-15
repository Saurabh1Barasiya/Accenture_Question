def sumrecs(number):
    if number%10==0:
        return number
    else:
        return number%10+sumrecs(number//10)
number = 123
val = sumrecs(number)
if val>10:
    print(val)
else:
    print("result is less then 10")
    

