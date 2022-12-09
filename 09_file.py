with open ("sample.txt","w") as f:
    data=f.write("Hello,I am sonu Ram")

with open("sample.txt","r") as f:
    data=f.read(5)
print(data)

with open("sample.txt","a") as f:
    data=f.write("\nI am python Developer")

with open("sample.txt","r") as f:
    data=f.read()
    f.close()

print(data)

