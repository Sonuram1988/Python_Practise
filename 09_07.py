file1="file1.txt"
file2="file2.txt"

with open (file1) as f:
    f1=f.read()

with open(file2) as f:
    f2=f.read()

if(f1==f2):
    print("Both files are same")
else:
    print("Both files are not same")
    