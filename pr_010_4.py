class Calculator:

    def cube(self, num):
        return num**3

    def square(self, num):
        return num**2

    def squareRoot(self, num):
        return num**0.5
    
    @staticmethod
    def greet():
        print("Thank u so much for this help")


c = Calculator()
print(c.cube(5))
print(c.square(3))
print(c.squareRoot(25))
Calculator.greet()
