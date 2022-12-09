class Employee:
    company="Google"

    def printDetail(self):
        print(f"I work in {self.company}")
        
    @staticmethod
    def greet():
        print('Hello! world')


e=Employee()
e.printDetail()
Employee.greet()


    