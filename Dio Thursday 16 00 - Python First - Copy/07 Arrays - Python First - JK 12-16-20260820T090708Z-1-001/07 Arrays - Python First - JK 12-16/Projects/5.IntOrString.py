entry = input("Please input a number or a string: ")

if entry.isalpha():
    print("You have inputted a string.")
elif entry.isdigit():
    print("You have inputted an integer.")

print("Thank you for using the program.")