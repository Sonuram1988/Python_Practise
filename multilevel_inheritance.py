class grandParent:
    company="Microsoft"

class Parents(grandParent):
    company="Skype"

class Child(Parents):
    name="Sonu Ram"
    def printDetails(self):
        print(f"{self.name} is working in {self.company}")

c1=Child()
c1.printDetails()
p1=Parents()
gp=grandParent()
print(p1.company)
print(gp.company)
