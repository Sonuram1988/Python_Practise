class Employee:
    company="Bharat Electrical"
    salary=5500
    salaryBonus=1000

    @property
    def totalSalary(self):
        return self.salary+self.salaryBonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.salaryBonus=val-self.salary

e=Employee()
print(e.totalSalary)
e.totalSalary=7000
print(e.salaryBonus)

