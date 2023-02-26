class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
        
    def annual_salary(self):
        return (self.pay*12)+self.bonus


class EmployeeOne:
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.agg_salary=sal

    def total_sal(self):
        return self.agg_salary.annual_salary()

salary=Salary(10000,1500)
# print(salary.annual_salary())
emp=EmployeeOne('Geek',25,salary)
print(emp.total_sal())

