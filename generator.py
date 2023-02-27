# def generator(num):
#     for i in range(num):
#         yield i

# x1=generator(10)
# print(next(x1))
# print(next(x1))
# print(next(x1))

def gen():
    yield 1
    yield 2
    yield 3

x=gen()
for i in x:
    print(i)
