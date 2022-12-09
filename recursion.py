num = int(input("Enter a number\n"))

# def factorial(num):
#     if num==0 or num==1:
#         return 1
#     else:
#         return num*factorial(num-1)


# fact=factorial(num)
# print(fact)

# n(n+1)/2
def sum(num):
    if num == 0 or num == 1:
        return 1
    else:
        return sum(num-1)+num


total = sum(num)
print(total)
