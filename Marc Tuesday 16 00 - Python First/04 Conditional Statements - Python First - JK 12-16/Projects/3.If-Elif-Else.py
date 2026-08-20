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
elif (randomNumber < 60):
    print("No. The random number is between 50 and 60")
elif (randomNumber < 70):
    print("No. The random number is between 60 and 70")
elif (randomNumber < 80):
    print("No. The random number is between 70 and 80")
elif (randomNumber < 90):
    print("No. The random number is between 80 and 90")
else:
    print("No. The random number is greater than 90!")