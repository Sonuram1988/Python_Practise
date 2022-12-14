list=[2,3,2,4,5,7,34,34,53,24,21]

# b=[]

# for item in list:
#     if item%2==0:
#         b.append(item)
# print(b)

# b=[i for i in list if i%2==0]
# print(b)

b={i for i in list}
print(b)