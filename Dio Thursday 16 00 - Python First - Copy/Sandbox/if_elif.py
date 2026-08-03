import random

#Variable
randomNumber = random.randrange(1,101)

#Instructions
print("This is a random generator. We have a variable with random value from 1 to 100 inside of it.")
print("If the value is less than 50, we'll let you know!")

print(f"The random number is: {randomNumber}")

#Conditional Statements
if randomNumber < 50:
    print("Yes! The random number is less than 50!")
    if randomNumber< 60:
        print("No. The random number is between 50 and 60")
        if (randomNumber < 70):
            print("No. The random number is between 60 and 70")