
from random import choice

print("\n...Rock... \n...Paper... \n...Scissors...")

r = "rock"
p = "paper"
s = "scissors"

player = input("player, please choose rock, paper or scissors: \n - ")

options = [r, s, p]

computer = choice(options)
print(f"The computer plays {computer}")
if player == computer:
    input("It's a draw. Let's play again")
elif player == "rock" and computer == "scissors":
    print("You Win")
elif player == "paper" and computer == "rock":
    print("You Win")
elif player == "scissors" and computer == "paper":
    print("You Win")
else:
    print("Computer wins")








