from random import randint
from sys import exit

username = input("Hello dear, what's your name: ")

player_1 = username
player_2 = "Moseph"
cards1 = []
for j in range(3):
    n1 = randint(2, 11)
    cards1.append(n1)
cardsT1 = cards1[0] + cards1[1] + cards1[2]

print(f"Hello {player_1} please draw three cards")

cards2 = []
for i in range(3):
    reply = input("a. Draw\nb. Quit\n").lower()
    if reply == "a":
        n = randint(2, 11)
        cards2.append(n)
    elif reply == "b":
        print("quiting...")
        exit()
 
cardsT = cards2[0] + cards2[1] + cards2[2]

print(f"your cards are: {cards2[0]}, {cards2[1]} and {cards2[2]}")
print(f"That's a total of {cardsT}\n{player_2} drew a total of {cardsT1}\n")

if cardsT > cardsT1 and cardsT in [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17,18, 19, 20, 21]:
    print("You have won the Blackjack game. Congrats.")
elif cardsT == cardsT1:
    print("That's a tie. Try again.")
else:
    print("You have lost this round, better luck next time.")
