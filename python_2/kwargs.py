def myfunc(**kwargs):
    for (name,value) in kwargs.items():
        print(name,value)


myfunc(fname='Sonu Ram',id='1001')