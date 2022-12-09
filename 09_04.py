words=["kadu","mote","Kameena","haramkhor"]
with open("sample.txt","r") as f:
    data=f.read()
# print(data)

# data=data.replace("kadu","#$%##@$")
# data=data.replace("kameena","##@#@!@#")
# data=data.replace("motu","#$%$$#$#")
# data=data.replace("haramkhor","#$%$$##$@")
for word in words:
    data=data.replace(word,"$#$##$$@#")
    with open("sample.txt","w") as f:
        f.write(data)