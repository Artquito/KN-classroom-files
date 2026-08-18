#Introduction
print("DIVISOR CALCULATOR PROGRAM")
print("Give me any number and I'll show you the divisors of the number.")

#Input
number = int(input("Number: "))

#Output
print(f"The divisors of {number} are:")

for count in range(1,number+1):
    if number % count == 0:
        print(count)