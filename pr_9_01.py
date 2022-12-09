
with open ("poem.txt","w") as f:
    f.write('''Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.''')

with open("poem.txt") as f:
    data=f.read()

if "twinkle" in data:
    print("twinkle is presented")