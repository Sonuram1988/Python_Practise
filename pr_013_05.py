from functools import reduce
num=[23,32,12,3,32,34,45,34,67,43,25,64]
greater_num=reduce(max,num)
print(greater_num)