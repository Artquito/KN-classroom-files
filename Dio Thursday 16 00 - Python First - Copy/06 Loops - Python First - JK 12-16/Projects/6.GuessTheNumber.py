#Import
import random

#Variable
number = random.randint(1,15)

#Introduction
print("GUESS THE NUMBER PROGRAM.")
print("Try to guess the number by using these hints:")

#Conditional Statements
if number <= 5:
    print("The number is less than or equals to 5.")
elif number > 5 and number <= 10:
    print("The number is greater than 5 but less than or equals to 10.")
elif number > 10 and number <= 15:
    print("The number is greater than 10 but less than or equals to 15.")

#Input
answer = int(input("What is your guess: "))

#Infinite Loop
while True:
    if answer != number:
        print("Wrong answer! Try it again.")
        answer = int(input("What is your guess: "))
    else:
        break

print("Congratulation. Your guess is correct.")