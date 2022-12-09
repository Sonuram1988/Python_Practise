class Parent:
    company="Google"
    def hello(self):
        print("Hello! world")

class Child(Parent):
    def hello(self):
        print("Hello!!!!")

c=Child()
print(c.company)
c.hello()
p=Parent()
p.hello()