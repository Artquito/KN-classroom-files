import random

dice = random. randint(1,6)
confirm = "yes"

print("DICE SIMULATOR")
print("You know how dice works :)")
print("Let's start!")

while confirm != "no":
    print(dice)
    confirm = input("Again? Press enter to continue. Type no if you want to stop the simulation.").lower()

    if confirm == "no":
        print("Thank you for using the program.")
        confirm = "no"

    dice = random.randint(1, 6)