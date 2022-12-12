class Employee:
    salary=30000
    increament=5000

    @property
    def totalSalary(self):
        return self.salary+self.increament

    @totalSalary.setter
    def totalSalary(self,sal):
        self.increament=sal-self.salary
    
e=Employee()
print(e.totalSalary)
e.totalSalary=50000
print(e.increament)


