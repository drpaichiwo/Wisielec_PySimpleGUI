import random
import string
import time
from slowa import words
from wisielec_ascii import wisielec_ascii_dict


# Game loop
def hangman():
    start_time = time.time()
    word = random.choice(words).upper()  # Generate a random word
    word_letters = set(word)   # Letters in the word
    alphabet = set(string.ascii_uppercase)  # Alphabet to choose from
    used_letters = set()  # Set of used letters
    lives = 10
    points = 0

    while len(word_letters) > 0 and lives > 0:

        # Letters used
        # 'separator'.join(['a', 'b', 'cd']) --> 'a b cd'
        print('Użyte litery: ', ' '.join(used_letters))
        print(f'Masz {lives} żyć')

        # What is the word (ie W _ R D)
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print(wisielec_ascii_dict[lives])
        print('Słowo: ', ' '.join(word_list))

        user_letter = input('Podaj literę: ').upper()  # Getting user input

        # Game rules
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1
                print('Pudło, spróbuj jeszcze raz')
        elif user_letter in used_letters:
            print('Ta litera już została użyta. Spróbuj jeszcze raz')
        elif user_letter not in alphabet:
            print('Użyj liter A-Z. Spróbuj jeszcze raz')

    # Win / Die ?
    # Gets here when len(word_letters == 0 or when lives == 0
    if lives == 0:
        print(f'Masz {lives} żyć i przegrałeś, słowo to: {word}')
    else:
        # How many seconds it took user to guess the word
        end_time = time.time()
        seconds = end_time - start_time
        # Add points
        points = points + 1
        # Print end statement
        print(f'Zgadłeś słowo {word} w czasie {round(seconds)} sekund')
        if points == 1:
            print(f'Zdobyłeś 1 punkt')
        elif 1 < points <= 4:
            print(f'Zdobyłeś {points} punkty')
        elif points > 4:
            print(f'Zdobyłeś {points} punktów')

    # Play again ?
    again = input('Jeszcze raz T/N ?: ').upper()
    if again == 'T':
        hangman()
    else:
        quit()


if __name__ == '__main__':
    hangman()