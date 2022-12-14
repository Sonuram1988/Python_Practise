
def readFile(fileName):
    try:
        with open(fileName,"r") as f:
            data=f.read()
            print(data)
    except FileNotFoundError as e:
        print(f"file not found {fileName}")
readFile("01.txt")
readFile("02.txt")
readFile("03.txt")
