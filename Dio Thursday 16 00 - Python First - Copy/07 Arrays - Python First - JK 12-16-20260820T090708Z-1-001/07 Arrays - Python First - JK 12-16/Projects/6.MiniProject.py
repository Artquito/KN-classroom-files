entry = 0
total = 0
numbers = []

#Opening and initial input
print("Please input a number to be calculated and press enter. If you are done")
print("please write 'Done' and press the enter key. Thank you!")
entry = input("Please input a number: ").lower()

while entry != "done":
    if entry.isalpha():
        print("Input is invalid")
    elif entry.isdigit():
        print("Your input is valid and has been added to the array.")
        numbers.append(entry)
        print("Currently the numbers that have been added is as follow: ")
        print(numbers)

    entry = input("Please input a number: ").lower()

for number in numbers:
    total += int(number)

print("Thank you for using the advance calculator!")
print(f"The total of your numbers is... {total}. Hope you enjoyed making it!")