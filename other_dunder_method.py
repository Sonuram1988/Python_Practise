class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("Let's add")
        return self.num+num2.num

    def __mul__(self, num2):
        print("Let's multiply")
        return self.num*num2.num

    def __str__(self):
        return f"Number is:{self.num}"

    def __len__(self):
        return 1


n1 = Number(4)
print(n1)  # <__main__.Number object at 0x0000000000438880>
print(len(n1))
