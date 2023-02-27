# def increament(num):
#     try:
#         num+=1
#         return num
#     except:
#         raise ValueError("It is a wrong value")
# print("Thanks for using this program")

# print(increament(56))

def division(num1,num2):
    try:
        ans=num1/num2
        return ans
    except:
        raise ValueError("You entered wrong value")

res=division(10,0)
print(res)


