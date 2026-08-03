#Imports
import random

#Variable
randomNumber = random.randrange(1,101)

#Instructions
print("This is a random generator. We have a variable with random value from 1 to 100 inside of it.")
print("If the value is less than 50, we'll let you know!")

print(f"The random number is: {randomNumber}")

#Conditional Statements
if (randomNumber < 50):
    print("Yes! The random number is less than 50!")
else:
    print("No. The random number is greater than 50!")