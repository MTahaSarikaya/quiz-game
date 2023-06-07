print("Soru oyunuma hos geldin!")

player = input("Do you want to start the game? ")
if player != "yes":
    quit()
print("Okay, let's play :) ")

score = 0


answer = input("Who is the most successful basketball player of all time? ")
if answer == "Michael Jordan":
    print("Correct!")
    score += 1
else: 
    print("Wrong!")

answer = input("Who is the most successful football player of all time? ")
if answer == "Lionel Messi":
    print("Correct!")
    score += 1
else: 
    print("Wrong!")

answer = input("Which is the highest mountain of the world? ")
if answer == "Mount Everest":
    print("Correct!")
    score += 1
else: 
    print("Wrong!")

answer = input("What is the most watched sport worldwide? ")
if answer == "football":
    print("Correct!")
    score += 1
else: 
    print("Wrong!")

print("You got " + str(score) + " answers correct!")
print("Well done! You got " + str((score / 4) * 100) + "%.")

// Sorular ve cevaplari dilendigi gibi degistirilebilir.
