class Employee:
    company="Google"
    salary=3000

    def __init__(self,firstName):
        self.firstName=firstName
        print(self.salary,self.firstName)

    def printDetail(self):
        print(f"I work in {self.company}")
        
    @staticmethod
    def greet():
        print('Hello! world')


e=Employee("Sonu")
e.printDetail()
Employee.greet()