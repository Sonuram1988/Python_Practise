try:
    num=int(input("Enter a number\n"))
    c=1/num
except Exception as e:
    print(e)
    exit()
finally:
    print("Thanks for using this prgram")