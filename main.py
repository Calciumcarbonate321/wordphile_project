import random
from words_list import word_list

word=random.choice(word_list).upper()
gameboard=list()
w=str()
haswon=False
dash_index=0
letter=str()

for ch in word:
    if random.randint(0,101) in range(0,34):
        w=ch
    else:
        w="_"
    gameboard.append(w)
print(gameboard)
print(word)

while not haswon:
    u=input("Enter your guess: ")
    if len(u)==1:
        for cha in gameboard:
            if cha=='_':
                dash_index=gameboard.index(cha)
                letter=word[dash_index]
            if u==letter:
                gameboard[dash_index]=u
    print(gameboard)

    if '_' not in gameboard:
        print("Congratulations, you have won.")
        haswon=True
    if u==word:
        print("Congratulations, you have guessed it.")
        haswon=True
