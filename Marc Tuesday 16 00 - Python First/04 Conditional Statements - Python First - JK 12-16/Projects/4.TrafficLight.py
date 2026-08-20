#Instruction
print("Hello! I need you to type the color of traffic light (red or yellow or green).")

#Input
color = input("Give me the color: ").lower()

#Conditional Statements
if color == 'red':
    print("STOP! It's Red!")
elif color == 'yellow':
    print("Be Careful friend.")
elif color == 'green':
    print("GO! Chase your dream!")
else:
    print("Are you sure? Are you from another planet? There's no such color in Earth's traffic light.")