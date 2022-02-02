# fibonacci series using generator.

def gen(n):
    a, b = -1, 1
    for i in range(n):
        c = a+b
        yield c
        a, b = b, c

for i in gen(10):
    print(i)