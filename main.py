import random
import time

print("Welcome to Hangman!!")

hangmanWords = [
    "elephant",
    "giraffe",
    "sunflower",
    "ocean",
    "mountain",
    "pineapple",
    "butterfly",
    "whale",
    "rainbow",
    "island",
    "ballet",
    "cinnamon",
    "mystery",
    "paradise",
    "jazz"
]

word = str(hangmanWords[random.randint(0, len(hangmanWords) - 1)])
wordView = ""
attempts = 0
for i in range(len(word)):
    wordView += "_"
print(wordView)

while "_" in wordView:

    letter = ""

    while len(letter) != 1:

        letter = str(input("Guess a letter: ")).lower()
        if len(letter) > 1:
            print("You can only guess 1 letter")
        if len(letter) < 1:
            print("You haven't guessed a letter!")

    if letter in word:
        print("You got this letter right!")
        indices = []
        for i, char in enumerate(word):
            if char == letter:
                indices.append(i)
        for index in indices:
            wordView = wordView[:index] + letter + wordView[index + 1:]
        print(wordView)

    else:
        print("You got this letter wrong!")
        attempts += 1
        if attempts != 8:
            print(f"Guesses left: {8 - attempts}")

    if attempts == 8:
        print("Game Over")
        print(f"The word is: {word}")
        break

if attempts != 8:
    print("You won!")
