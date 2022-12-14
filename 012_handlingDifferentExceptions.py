
try:
    num=int(input("Enter a number\n"))
    div=1/num
    print(div)
except ValueError as e:
    print("Please enter a valid value")
    print(e)
except ZeroDivisionError as e:
    print("Make sure you are not dividing by zero")
    print(e)
print("Thanks for using this program")