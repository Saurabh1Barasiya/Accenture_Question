# check palindrom

def isPalindrom(s):
    return s == s[::-1]
n = str(121)
check = isPalindrom(n)
print(check)
if check:
    print("Number is palindrom")
else:
    print("Number is not palindrom")

