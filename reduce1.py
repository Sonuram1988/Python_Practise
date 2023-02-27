from functools import reduce

numbers=[12,15,3,4,14,20]
def sum(a,b):
    return a+b

ans=reduce(sum,numbers)
print(ans)