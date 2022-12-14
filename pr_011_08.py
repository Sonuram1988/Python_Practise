import random
randNum=random.randint(1,100)
print(randNum)
userGuess=0
guesses=0
while(userGuess!=randNum):
    userGuess=int(input("Enter a number:\n"))
    guesses+=1
    if userGuess==randNum:
        print("you guess right number")
    else:
        if(userGuess<randNum):
            print("you guess wrong number!!!Please enter a larger number")
        if(userGuess>randNum):
              print("you guess wrong number!!!Please enter a smaller number")
print(f"yours total guesses is {guesses}")
with open("hiscore.txt","r") as f:
    hiscore=int(f.read())
    if(hiscore>guesses):
        print("you have broken hiscore record")
        with open("hiscore.txt","w") as f:
            f.write(str(guesses))
            

