#Import
import random

#Variables
num1 = random.randint(1,100)
num2 = random.randint(1,100)
operator = random.randint(1,3)
result = 0
operator_sign = ""
answer = 0

#Conditional Statements
if operator == 1:
    result = num1 + num2
    operator_sign = "+"
elif operator == 2:
    result = num1 - num2
    operator_sign = "-"
elif operator == 3:
    result = num1 * num2
    operator_sign = "*"

#Introduction
print("MATH QUIZ PROGRAM.")
print("Just answer the question :)")

print(f"What is {num1} {operator_sign} {num2}?")

#Infinite Loop
while True:
    answer = int(input("Answer: "))

    if answer == result:
        print("Correct!")
        break
    else:
        print("Wrong.")

print("Thanks for playing :)")
