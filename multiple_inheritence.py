class A1:
    company="Google"
    def info(self):
        print("This is A1 class")

class B1:
    company="Youtube"
    def printDetails(self):
        print(f"my company is {self.company}")

class Merge_A1_B1(A1,B1):
    company="Android"
    def details_Info(self):
        print(f"This is {self.company}")

a1=A1()
print(a1.company)
b1=B1()
b1.printDetails()
c1=Merge_A1_B1()
c1.details_Info()
print(c1.company)
c1.info()