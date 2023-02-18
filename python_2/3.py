# Enter number of terms needednbsp;#0,1,1,2,3,5....
num=int(input("Enter how many turn,you want?"))
a=0
b=1
print(a)
print(b)

for x in range(2,num):
    sum=a+b
    print(sum)
    a=b
    b=sum
