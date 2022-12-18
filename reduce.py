from functools import reduce

l1 = [2, 5, 6, 42, 443, 13, 34, 53, 13, 34, 5, 134, 44]
def sum(a, b): return a+b


total = reduce(sum, l1)
print(total)
