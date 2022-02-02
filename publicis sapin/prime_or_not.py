# check given number is prime or not using for loop
num = int(input("Enter a number: ")) 
if num == 1 or num == 0:
    print("Not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime",i)




# check given number is prime or not using while loop
# num = int(input("Enter a number: ")) 
# if num == 1 or num == 0:
#     print("Not prime")
# else:
#     i = 2
#     while i < num:
#         if num%i==0:
#             print("Not prime")
#             break
#         i += 1
#     else:
#         print("Prime")