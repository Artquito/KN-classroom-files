cars = ["Volvo", "Mazda", "Kia"]

print("Below are the initial cars:")
print(cars) 

#Append
cars.append("Nissan")
print("Below are the arrays after adding a new car to the array:")
print(cars)

#Delete
del cars[0]
print("Below are the arrays after deleting the car inside index 0: ")
print(cars)

#Remove
cars.remove("Kia")
print("Below are the arrays after deleting the car called Kia")
print(cars)