# def div(num):
#     return num%5==0

l1=[45,43,35,30,25]
# new_L2=filter(div,l1)
new_L2=filter(lambda num:num%5==0,l1)
print(list(new_L2))