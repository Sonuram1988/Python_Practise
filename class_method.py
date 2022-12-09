class Employee:
    company="Google"
   
    # def hello(self,comp):
        # self.__class__.company=comp
    @classmethod
    def hello(cls,comp):
        cls.company=comp
        print(f"This is hello function,{Employee.company}")

e=Employee()
# e.hello()
# Employee().hello()
Employee.hello("Apple")
print(Employee.company)
