
while(True):
    print("press q to exit")
    num=input("Enter a number\n")
    if num=='q':
        break
    try:   
        num=int(num)
        if num>6:
            print("Yours entered number is greater than 6")
    except Exception as e:
        print("yours enter number is wrong")
print("Thanks! for playing this game")
