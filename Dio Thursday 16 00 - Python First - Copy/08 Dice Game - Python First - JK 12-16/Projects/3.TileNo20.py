import random

dice = random.randint(1,6)
finish = "False"
stepcounter = 0
tile = 0
highscore = 20

print("Welcome to Tile No 20 Game.")
print("Test your luck and see how long it'll take you to the finish line.")
print("The finish line should be on tile no. 20.")
print(f"Currently, the high score for the game is {highscore}.")

while finish != "True":
    input("Press enter to roll the dice")
    dice = random.randint(1, 6)
    print(f"You got {dice}.")
    stepcounter += 1
    tile += dice

    if tile <= 20:
        print(f"Keep going. You are still on tile number {tile}.")
    else:
        print("Congratulation! You reached tile number 20.")
        print(f"You finished the game in {stepcounter} steps.")

        if stepcounter < highscore:
            print("Nice! That is a new high score!")
            highscore = stepcounter
        else:
            print("Thanks for playing! You didn't reach the high score. Better luck next time.")

        answer = input("Do you want to play again?(y/n) ").lower()

        if answer == "y":
            stepcounter = 0
            tile = 0
            print("Good luck friend!")
        elif answer == "n":
            print("Thanks for playing.")
            finish = "True"
        else:
            print("Invalid respond. I am going to take that as a no.")
            print("See you later.")
            finish = "True"