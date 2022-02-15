def fict(n):
    if n == 0:
        return 1
    else:
        return n * fict(n-1)
print(fict(5))