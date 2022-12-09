# a=10
# b=20

# print(a+b)

class Sum:
    # def total(self,a,b):
    #     self.a=a
    #     self.b=b
    #     return self.a+self.b

    def total(self):
        return self.a+self.b


s = Sum()
# print(s.total(30,40))
s.a = 10
s.b = 20
print(s.total())
