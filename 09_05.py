
content=True
i=0
with open("sample1.txt","r") as f:
    while(content):
        data=f.readline()
        if "python" in data:
            print(f"Python is present in line no.{i}")
        i+=1