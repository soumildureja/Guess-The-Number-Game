import random
n1=input("WELCOME TO THE GUESS THE NUMBER GAME\nARE YOU READY TO PLAY?\n(Y) FOR YES\n(N) FOR NO\n")
if n1=="Y":
    print("LETS BEGIN")
    print("Guessing Number Is Between 11-20")
    print("You Get Ony Nine Chances To Guess The Correct Number")
else:exit()
n2=random.randrange(11,20)
guesses=1
while(guesses<=9):
    try:
        i=int(input("Enter Your Guessing Number\n"))
    except:
        print(" ")
    if i>n2:
        print("Enter Some Smaller Value\n")
    elif i<n2:
        print("Enter Some Bigger Value\n")
    else:
        print("You Won")
        print(guesses, "Number Of Guesses You Took To Finish")
        break

    print(9 - guesses, "no. of guesses left")
    guesses = guesses + 1

if (guesses > 9):
    print("Game Over")