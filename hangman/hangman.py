import random

words = ["brambor", "pole", "seznam", "abeceda", "asfalt"]
picked_word = words[random.randint(0, len(words) - 1)]
lives = 5
correct_letters = set()
score = 0

print("Ahoj! Vítej ve hře HANGMAN")


while lives > 0:
    guess_letter = str.lower(input("Jaké písmeno si myslíš? > "))

    if guess_letter in picked_word:
        if guess_letter not in correct_letters:
            correct_letters.add(guess_letter)
            score += 1
        else:
            print("Pismeno už jsi uhádl, zkus jiné")
    else:
        lives -= 1
        print("Špatně...")
        print(f"Počet zbývajících pokusů: {lives}")

    for p in picked_word:
        if p in correct_letters:
            print(p, end=" ")
        else:
            print("_", end=" ")

    if score == len(set(picked_word)):
        print("Winner, winner, chicken dinner!")
        break

    if lives == 0:
        print(f"Prohrál jsi. Slovo bylo: {picked_word}")
