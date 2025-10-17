import random

# Step 1: Choose a word
words = ["python", "hangman", "apple", "computer", "future"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6  # Number of wrong guesses allowed
used_letters = []

print("Welcome to Hangman!")

# Step 2: Main game loop
while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Used letters:", ", ".join(used_letters))
    print(f"Attempts left: {attempts}")
    
    guess = input("Guess a letter: ").lower()
    
    if guess in used_letters:
        print("You already guessed that letter.")
        continue
    
    used_letters.append(guess)
    
    if guess in word:
        print("Good guess!")
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

# Step 3: End of game
if "_" not in guessed:
    print("\n🎉 You win! The word was:", word)
else:
    print("\n💀 You lose! The word was:", word)
