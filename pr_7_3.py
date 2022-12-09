num=int(input("Enter a number\n"))
count=0

for i in range(2,num):
    if num%i==0:
        count+=1

if(count==1):
    print(f"{num} is not prime")
else:
    print(f"{num} is prime")
        