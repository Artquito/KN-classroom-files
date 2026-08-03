import random

tebakAngka = random.randint(1, 10)
print("Ayooooo tebak angka ini!!!!! angkanya dari 1 sampai 10")
angka = input("Kamu tebak angka berapa? ")

print(f"Kamu tebak angka {angka}")

if angka == str(tebakAngka):
    print(f"Tebakannya benar")
else:
    print("Tebakannya salah")

print(f"Jawabannya adalah {tebakAngka}")