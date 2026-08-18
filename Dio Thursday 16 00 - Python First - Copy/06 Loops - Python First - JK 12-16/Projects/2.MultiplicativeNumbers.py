#Variables
counter = 0
result = 0

#Intro
print("MULTIPLICATIVE NUMBERS PROGRAM.")
print("Give me any number and then I will show you the multiplicatives of that number until 10 numbers long.")

#Input
number = int(input("Number: "))

#Output
print(f"The multiplicatives of {number} are:")

#Loop
while counter < 10:
    result += number
    print(result)
    counter += 1