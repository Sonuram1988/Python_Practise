# complex numbers

class Complex:
    def __init__(self,r,i):
        self.imaginary=i
        self.real=r

    def __add__(self,c):
        return Complex(c.real+self.real,c.imaginary+self.imaginary)
    
    def __str__(self):
        return f"{self.real}+{self.imaginary}i"

c1=Complex(2,4)
c2=Complex(1,2)
sum=c1+c2
print(sum)
