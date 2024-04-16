import random
from dictionary_words import generate_random_word

def play_game():
    word_dict = generate_random_word()
    word = word_dict["word"]
    meaning = word_dict["meaning"]

    print(f'it is a {len(word)} letters word.')
    print(f'Meaning: {meaning}\n')

    turns = 10
    guessed_letters = []

    while turns > 0:
        print(f'You have {turns} chances left')
        display_word = ''.join([letter if letter in guessed_letters else '-' for letter in word])# Displaying word with guessed letters
        print(display_word)

        if display_word == word:
            print('Congartulations', name)
            print('You won!\nthe word is:', word, 'with meaning:', meaning, "\n")
            break

        guess = input('Enter a letter or type "hint" for a hint: ').lower()

        if guess == "hint":
            hint_letter = random.choice([c for c in word if c not in guessed_letters])
            print(f"Hint: The word contains the letter '{hint_letter}'")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            turns -= 1
            print('Incorrect guess! Try again.\n')

        if turns == 0:
            print('You lost!\nThe word was:', word, 'with meaning:', meaning)
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_game()

if __name__ == "__main__":
    name = input('Enter your name: ')
    print('Good Luck!', name)
    print('Guess the word\n')
    print('\t\t*****RULE BOOK*****')
    print('1) Enter only lowercase single alphabet, input like "swn" is invalid')
    print('2) You have 10 tries to accomplish your target.')
    print('3) It is guaranteed that the lucky word is in lowercase only.\n')

    play_game()
