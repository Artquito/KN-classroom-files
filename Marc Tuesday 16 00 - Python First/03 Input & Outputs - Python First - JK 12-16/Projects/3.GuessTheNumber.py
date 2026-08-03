import random

compNumber = random.randrange(1,4)

print("Hi, this is Random Number Program. I am thinking of a number between 1 to 3.")
answer = input("Can you guess what number it is? ")

print(f"The answer is: {compNumber == int(answer)}")
print(f"The correct number is: {compNumber}")
