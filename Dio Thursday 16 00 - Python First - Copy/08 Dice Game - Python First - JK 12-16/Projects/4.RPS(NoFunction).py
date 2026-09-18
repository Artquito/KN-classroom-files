import random

weapons = ["rock", "paper", "scissor"]
player = ""
enemy = ""
end = False
answerCheck = False

print("ROCK, PAPER, SCISSOR GAME.")
print("You know how the rock paper scissor game works.")
print("Just play it :)")

while end != True:
    answerCheck = False
    print("Rock, Paper, Scissor, Shoot!")
    answer = int(input("Please select your weapon. 0 for rock, 1 for paper, 2 for scissor."))
    enemy = random.choice(weapons)

    while answerCheck != True:
        if answer == 0 or answer == 1 or answer == 2:
            answerCheck = True
            player = weapons[answer]

            if player == "rock" and enemy == "scissor" or player == "paper" and enemy == "rock" or player == "scissor" and enemy == "paper":
                print(f"The enemy was picking {enemy}.")
                print("You won! Congratulations!")
                end = True

            elif player == enemy:
                print(f"Draw! The enemy was picking {enemy} as well.")
                print("Let's try again.")

            else:
                print(f"The enemy was picking {enemy}.")
                print("You lose! Better luck next time.")
        else:
            print("Your input is invalid. Please try again.")
            answerCheck= True