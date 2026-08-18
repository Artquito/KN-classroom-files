#Intoduction
print("HI, I AM PYTHON BOT.")
print("Do you want to play with me? (y/n)")

#Input
answer = input("Answer: ").lower()

#Infinite Loop
while True:
    if answer != "y":
        print("I am giving you another chance. Do you want to play again? (y/n)")
        answer = input("Answer: ").lower()
    else:
        break

print("Thanks for playing with me :)")