num=int(input("Enter a number\n"))
n=0

for i in range(2,num):
    if(num%i==0):
        n=n+1
    
if(n>1):
        print(f"{num} is not prime")
else:
    print(f"{num} is prime")