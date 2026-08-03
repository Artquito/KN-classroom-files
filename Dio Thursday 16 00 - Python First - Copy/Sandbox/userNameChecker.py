print("Hello!")
print("This is a username validator. We'll check if your username is qualifying to our standards or not.")
print("Our username standards:")
print("1. The username characters at least 5 characters, but no more than 10 characters.")
print("2. The username should be all in lowercase.")

#Input
username = input("Input your username: ")

print(len(username))
# jika panjang username < 5 atau panjang username > 10
# maka print ("The character length is not qualified. Remember: At least 5 but no more than 10 characters")
# else
 # maka print("your username is qualified")