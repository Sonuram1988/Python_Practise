class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_salary(self):
        return (self.pay*12)+self.bonus
    

class Employee:
    def __init__(self,name,age,pay,bonus):
            self.name=name
            self.age=age
            self.obj=Salary(pay,bonus)

    def total_salary(self):
        return self.obj.annual_salary()

e=Employee('sonu',34,1000,1500)
print(e.total_salary())
        