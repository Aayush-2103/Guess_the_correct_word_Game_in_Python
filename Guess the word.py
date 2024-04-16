import random
from dictionary_words import generate_random_word

def play_game():
    word_dict = generate_random_word()
    
    randomWord = word_dict["word"]
    meaning = word_dict["meaning"]

    print(f'it is a {len(randomWord)} letters word.')
    print(f'Meaning: {meaning}')

    Str = "-" * len(randomWord)

    counter = 0  
    incorrect_guesses = []
    hint_used = False

    while counter < 10:
        print(f'You have {10 - counter} chances left')
        print(f'Incorrect guesses: {incorrect_guesses}\n\n{Str}\n')
        letter = input('Enter a letter or type "hint" for a hint: ')
        letter = letter.lower()

        if letter == "hint":
            if not hint_used:
                hint_letter = random.choice([c for c in randomWord if c not in Str])
                print(f"Hint: The word contains the letter '{hint_letter}'")
                hint_used = True
            else:
                print("Sorry, you can only use the hint once per game.")
            continue

        if len(letter) != 1 or not letter.isalpha():
            print("Please enter only one alphabetical character.")
            continue

        found = False
        for i, char in enumerate(randomWord):
            if char == letter:
                if Str[i] == '-':
                    Str = Str[:i] + letter + Str[i+1:]
                    found = True
                    break

        if not found:
            counter += 1
            incorrect_guesses.append(letter)

        print(Str)

        if Str == randomWord:
            print('Congartulations', name)
            print('You won!\nthe word is:', randomWord, 'with meaning:', meaning, "\n")
            break

        if counter == 10:
            print('You lost!\nThe word was:', randomWord, '----with meaning:', meaning, "\n")
            break

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()

if __name__ == "__main__":
    name=input('Enter your name:- ')
    print('Good Luck!', name)
    print('Guess the word\n')
    print('\t\t**RULE BOOK**')
    print('1) Enter only lowercase single alphabet, input like "swn" is invalid')
    print('2) You have 10 tries to accomplish you target.')
    print('3) It is guaranted that the lucky word is in lowercase only.\n\n')
    play_game()