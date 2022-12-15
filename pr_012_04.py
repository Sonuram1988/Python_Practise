
try:
    def div(num):
        val=1
        ans=val/num
        print(ans)
except ZeroDivisionError as e:
        print(e)

num=int(input("Enter a number:\n"))
div(num)

