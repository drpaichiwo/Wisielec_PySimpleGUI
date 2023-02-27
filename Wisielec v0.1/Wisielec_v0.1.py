import random
from ascii_art import hangman_art
from word_dictionary import words

# get random word
word = random.choice(words).upper()


# word letters as list
word_letters = [i for i in word]
# hidden letters as list
word_blanks = ["*"] * len(word)

# list with polish alphabet
alphabet = ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę',
            'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł',
            'M', 'N', 'Ń', 'O', 'Ó', 'P', 'R', 'S',
            'Ś', 'T', 'U', 'W', 'Y', 'Z', 'Ź', 'Ż']

lives = 10
guessed_letters = ""

while lives > 0:

    user_input = input("Podaj literę:").upper()

    # Check if user_input in guessed letters
    if user_input not in guessed_letters:
        guessed_letters += user_input
        print(guessed_letters)

        # Check if user_input in word_letters list
        if user_input in word_letters:
            print("Brawo. zgadłeś literę!")

            # find indexes of correctly guessed letter
            for i, letter in enumerate(word_letters):
                # and replace blanks with letters
                if word_letters[i] == user_input:
                    word_blanks[i] = word[i]
            # output updated word
            print("".join(word_blanks))

            # win condition
            if "".join(word_blanks) == "".join(word_letters):
                print("win")

        # lost condition
        else:
            print(f"Pudło. życia: {lives}")
            lives = lives - 1
            print("".join(word_blanks))
            if lives == 0:
                print("Lost")

    # output if letter already been chosen
    else:
        print(f"ta litera już była. Życia: {lives}")
