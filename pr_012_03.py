num=int(input("Enter a number:\n"))

table=[num*i for i in range(1,10+1)]
with open("tables.txt","a") as f:
    f.write(str(table))
    f.write("\n")
print(table)