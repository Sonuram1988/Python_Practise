with open("file1.txt") as f:
    data=f.read()

with open("file2.txt",'w') as f:
    f.write(data)