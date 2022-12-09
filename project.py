import random

def gameWin(comp,you):
    if comp is 's' and you is 'w':
        return False
    elif comp is 'w' and you is 'g':
        return False
    elif comp is 'g' and you is 's':
        return False
    elif comp==you:
        return None
    else:
        return True

print("computer's turn Snake(s),water(w) or gun(g)?\n")
random_num=random.randint(1,3)
print(random_num)
if random_num==1:
    comp="s"
if random_num==2:
    comp="w"
if random_num==3:
    comp="g"

you=input("Player's turn turn Snake(s),water(w) or gun(g)?\n")
result=gameWin(comp,you)

print(f"comp's choice is {comp}")
print(f"your choice is {you}")

if result is True:
    print("You are winner")
elif result is False:
    print("You are looser")
else:
    print("Game is tie")




