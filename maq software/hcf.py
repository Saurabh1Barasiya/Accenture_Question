a = 15
b = 10
mn =a if a<b else b
print("minimum value is:",mn)

for i in range(mn,1,-1):
    if (a%i == 0) and (b%i == 0):
        gcd = i
        print("GCD is:",gcd)
        break
# print("GCD is:",gcd)