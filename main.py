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
    user_input=u[0]

    for cha in gameboard:
        if cha=='_':
            dash_index=gameboard.index(cha)
            letter=word[dash_index]
        if user_input==letter:
            gameboard[dash_index]=user_input
    print(gameboard)
