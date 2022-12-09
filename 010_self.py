class Student:
    def extraInfo(self,name):
        self.name=name
        return self.name

s=Student()
value=s.extraInfo("Sonu Ram")
# value=Student.extraInfo(s,"Sonu Ram")
print(value)
