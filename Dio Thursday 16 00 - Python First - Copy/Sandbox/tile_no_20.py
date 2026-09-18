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

while finish ___ True:
    in___("Press enter to roll the dice")
    dice = random.randint(_, _)
    stepcounter ___ 1
    tile _= dice

    if tile <= ___:
        print(f"Keep going. You are still on tile number {___}.")
    else:
        print("Congratulation! You reached tile number 20.")
        print(f"You finished the game in {stepcounter} steps.")

        if stepcounter < highscore:
            print("Nice! That is a new high score!")
            highscore = stepcounter
        else:
            print("Thanks for playing! You didn't reach the high score. Better luck next time.")

        answer = input("Do you want to play again?(y/n) ").lower()
        if answer == __:
            stepcounter = 0
            tile = 0
            print("Good luck friend!")
        elif answer == __:
            print("Thanks for playing.")
            finish = "True"
        else:
            print("Invalid respond. I am going to take that as a no.")
            print("See you later.")
            finish = "True"