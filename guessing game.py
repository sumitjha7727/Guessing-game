import random

jackpot=random.randint(1,100)

print("the jackpot number is" ,jackpot)

guess=int(input("Guess kar bro : "))

counter=1

while guess!=jackpot:
    if guess<jackpot:
        print("Galat hai bro, guess higher : ")
    else:
        print("Galat hai bro, guess lower : ")
    guess=int(input("Firse guess kar : "))

    counter = counter+1
  
print("sahi jawab !!!",counter)
