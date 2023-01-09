import random

with open("wordlist.txt", "r") as file: #r is read lol
    allText = file.read()
    words = list(map(str, allText.split("\n")))
  
answer = (random.choice(words))

thislist = []

for ans in answer:
    thislist.append(ans)

#print(thislist)

guess = 0
i = 0

print("Wordle! You have 5 guesses.\n")

while i < 5:
    z = 0
    guess = input("Guess: ")
    if len(guess) != 5:
        print("Guess must be 5 letters. Try again.\n")
    else:
        for letter in guess:
            if letter == thislist[z]:
                print(letter + " is correct")
            elif letter in thislist:
                print(letter + " is in the wrong place")
            else:
                print(letter + " is incorrect")
            z += 1
    if guess == answer:
        input("Solved! The answer was " + answer)
        break
    i += 1
    if i == 5:
        input("Took too many attempts. Answer was " + answer)
        break