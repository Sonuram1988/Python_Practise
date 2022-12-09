class Programmer:
    company="microsoft"

    def __init__(self,firstName,subunit,salary):
        self.firstName=firstName
        self.subunit=subunit
        self.salary=salary
    
    def printDetails(self):
        print(self.company,self.subunit,self.firstName,self.salary)
    

p=Programmer("Sonu Ram","Azure",30000)
p1=Programmer("shiva","git",30000)
p.printDetails()
p1.printDetails()