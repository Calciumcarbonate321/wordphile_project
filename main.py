import random
from words_list import word_list
import time

#VARIABLE INITIALIZATIONS
word=random.choice(word_list).upper()
gameboard=list()
w=str()
haswon=False
dash_index=0
letter=str()
counter=5

for ch in word:
    if random.randint(0,101) in range(0,34):
        w=ch
    else:
        w="_"
    gameboard.append(w)

print("Welcome to WORDPHILE\n")
print("You have 5 lives in total. When you guess a word wrong, you will lose 1 life. When you lose all your lives, you die.\n")
print("Let the game begin!")

time.sleep(0.1)
for i in range(0,5):
    print(".....finding a word")
    time.sleep(1)

print(gameboard)


while not haswon:
    u=input("\nEnter your guess: ")
    if len(u)==1:
        for cha in word:
            if u == cha:
                w_index= word.index(cha)
                if gameboard[w_index]==cha:
                    print("\nYour guess is already in the word. You now have ",counter," lives left.\n ")
                elif gameboard[w_index]=='_':
                    gameboard[w_index]=cha

        if u not in word:
            counter-=1
            print("You have guessed wrong. You now have ",counter," lives left\n")
    if counter==0:
        print("You are already dead.")
        time.sleep(1)
        print("Thank you for playing our game.\n Have a nice day!")
        time.sleep(0.5)
        break
    print(gameboard)
    if '_' not in gameboard:
        print("Congratulations, you have won.")
        time.sleep(0.5)
        print("Have a nice day!")
        time.sleep(0.75)
        haswon=True

    if u==word:
        print("Congratulations, you have guessed it correctly.")
        time.sleep(0.5)
        print("Have a nice day!")
        time.sleep(0.75)
        haswon=True
