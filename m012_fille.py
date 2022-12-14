def greet(name):
    print(f"Good morning!, {name}")

print(__name__)
if __name__ == "__main__":
    name = input("Enter a name\n")
    greet(name)
