import copy
l1 = [1,2,3,4,5,6]
l2 = l1
# l2 = l1.copy()
print(l1)
print(l2)

l2.pop()
print("after popping")
print(l1)
print(l2)

print(id(l1)==id(l2))