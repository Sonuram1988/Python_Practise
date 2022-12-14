# complex numbers
#(a+bi)(c+di) = (ac−bd) + (ad+bc)i

class Complex:
    def __init__(self,r,i):
        self.imaginary=i
        self.real=r

    def __add__(self,c):
        return Complex(c.real+self.real,c.imaginary+self.imaginary)
    
    def __mul__(self,c):
        mulReal=c.real*self.real-c.imaginary*self.imaginary
        mulimaginary=c.imaginary*self.real+c.real*self.imaginary
        return Complex(mulReal,mulimaginary)
    
    def __str__(self):
        return f"{self.real}+{self.imaginary}i"
    

c1=Complex(3,2)
c2=Complex(1,7)
sum=c1+c2
print(sum)
mul=c1*c2
print(mul)
