class Employee:
    company = "Google"


e = Employee()
print(e.company)
Employee.company = "Youtube"
print(e.company)
e.company="Oracle"
print(e.company)
print(Employee.company)