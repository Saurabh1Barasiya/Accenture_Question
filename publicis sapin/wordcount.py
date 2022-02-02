s = "aabbccc"
unique_elements = []
for i in s:
    if i not in unique_elements:
        unique_elements.append(i)

for i in unique_elements:
    print(f"{i}{s.count(i)}",end="")

