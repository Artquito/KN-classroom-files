#Instructions
print("Hello!")
print("This is a username validator. We'll check if your username is qualifying to our standards or not.")
print("Our username standards:")
print("1. The username characters at least 5 characters, but no more than 10 characters.")
print("2. The username should be all in lowercase.")

#Input
username = input("Input your username: ")

#Conditional Statements
if len(username) < 5 or len(username) > 10:
    print("The characters length is not qualified. Remember: At least 5 but no more than 10 characters.")
elif not username.islower():
    print("The characters is not qualified. The characters should be all in lowercase.")
else:
    print("Your username is qualified.")
