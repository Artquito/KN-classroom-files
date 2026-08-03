aliceFavFood = "Cookies"
totalCookies = 7

johnFavFood = "Cake"
totalCakes = 10

print('Lie Detector:')
print(f"Alice Statement: My favorite food is cookies and I have more than 5 cookies.")
print("Detecting Alice's statement...")
print(f"Alice statement is {aliceFavFood == 'Cookies' and totalCookies > 5}")
print("")
print('Lie Detector:')
print(f"John Statement: My favorite food is cookies and I have more than 5 cookies.")
print("Detecting John's statement...")
print(f"John statement is {johnFavFood == 'Cookies' and totalCakes > 5}")
print("")
print(f"Another statement: John or Alice has exactly 10 foods.")
print(f"The statement is {totalCookies == 10 or totalCakes == 10}")