def natrual_sum(n):
    if n == 0:
        return 0
    else:
        return n + natrual_sum(n-1)
print(natrual_sum(10))

# n = 10
