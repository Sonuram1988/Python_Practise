# list=["Sonu","Dog","Apple","Python"]
# list.remove("Sonu")
# print(list)


# word="   Sonu is good boy  "
# print(word)
# word=word.strip()
# print(word)

def remove_split(string):
    newStr=string.replace("Sonu"," ")
    return newStr.strip()

str=remove_split("Sonu is good boy  ")
print(str)