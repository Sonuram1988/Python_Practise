def greater_than_5(num):
    if num>5:
        return True
    else:
        return False

l1=[2,3,4,54,53]
newList=filter(greater_than_5,l1)
print(list(newList))