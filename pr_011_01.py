class C2dVec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    
    def __str__(self):
        return f"{self.icap}i+{self.jcap}j"
    
class C3dVec(C2dVec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k
    
    def __str__(self):
        return f"{self.icap}i+{self.jcap}j+{self.kcap}k"

c2dvec=C2dVec(2,3)
c3dvec=C3dVec(1,3,4)
print(c2dvec)
print(c3dvec)
