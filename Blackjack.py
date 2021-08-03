#Blackjack_capstone

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def getrandom():
    randomcard = cards[random.randint(0,len(cards) - 1)]
    return randomcard
    
userhand = []
    
pchand = []    
    
userfirst = str(getrandom())
usersecond = str(getrandom())

userhand.append(userfirst)
userhand.append(usersecond)
userscore = int(userhand[0])+ int(userhand[1])

pcfirst = str(getrandom())
pcsecond = str(getrandom())

pchand.append(pcfirst)
pchand.append(pcsecond)
pcscore = int(pchand[0]) + int(pchand[1])

if (pcscore or userscore >= 21):
    if pcscore == 21:
        print("Computers got blackjack! You lose.")
    elif userscore == 21 and pcscore < 21:
        print("You got blackjack! You win!")
    elif userscore > 21:
        print("You busted! You lose.")

if userscore or pcscore > 21:
    cards[0] = 1
else:
    cards[0] = cards[0]

print(f"Your score is {userscore}")

print(f"Your hand: \n {userhand}")
      
print(f"Computer's score is {pcscore}")

print(f"Computer's hand: \n {pchand[0]} \n")
