def increament(num):
    try:
        num+=1
        return num
    except:
        raise ValueError("It is a wrong value")
print("Thanks for using this program")

print(increament(56))
