a=54 # global variable
def hello():
    global a
    print(a)
    a=8 # Local variable
    print(a)

hello()
print(a)


