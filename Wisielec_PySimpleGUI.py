# Wisielec with PySimpleGUI

import PySimpleGUI as sg
import random
from word_dictionary import words
from hangman_art import hangman_art

sg.theme("black")
font_used = "Young"
layout = [
    [sg.Image(hangman_art[10], key="-HANGMAN-")],
    [sg.Text("", key="-WORD-", font="Young 20")],
    [sg.Text("użyte litery", font=font_used)],
    [sg.Text("", key="-USED-LETTERS-", font=font_used)],
    [sg.Text("życia", font=font_used),
     sg.Text("", key="-LIVES-", font="Young 16", text_color="green"),
     sg.Push(),
     sg.Text("0", key="-POINTS-", font="Young 16", text_color="green"),
     sg.Text("punkty", font=font_used)],
    [sg.Text("Podaj literę:", font=font_used)],
    [sg.Input("", size=(10, 1),
              enable_events=True,
              key="-INPUT-")],
    [sg.Button('Submit', visible=False, bind_return_key=True)],
    [sg.Text("", key="-OUT-", font="Any 10", text_color="yellow")],
    [sg.VPush()]
]

window = sg.Window("Wisielec", layout,
                   size=(300, 550),
                   element_justification="center",
                   finalize=True)


def hangman():

    # list with polish alphabet
    alphabet = ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł',
                'M', 'N', 'Ń', 'O', 'Ó', 'P', 'R', 'S', 'Ś', 'T', 'U', 'W', 'Y', 'Z', 'Ź', 'Ż',
                'a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł',
                'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż']

    # word choice
    word = random.choice(words).upper()
    # word letters as list
    word_letters = [i for i in word]
    # word blanks as list
    word_blanks = ["_"] * len(word)
    # number of tries
    lives = 10
    # points
    points = 0
    # letters already used
    guessed_letters = ""

    # Main Loop
    while lives > 0:

        window["-HANGMAN-"].update(hangman_art[lives])
        window["-WORD-"].update("".join(word_blanks), font="Young 24")
        window["-USED-LETTERS-"].update(", ".join(guessed_letters))
        window["-LIVES-"].update(lives)

        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        # accepts only one character, must be from alphabet
        if len(values["-INPUT-"]) > 1 or values["-INPUT-"] not in alphabet:
            # delete last char from input
            window["-INPUT-"].update(values["-INPUT-"][:-1])
        # if enter is pressed
        elif event == 'Submit':
            user_input = window["-INPUT-"].get().upper()
            window['-INPUT-'].update("")

            # Check if user_input in guessed letters
            if user_input not in guessed_letters:
                guessed_letters += user_input
                window["-USED-LETTERS-"].update(", ".join(guessed_letters))

                # Check if user_input is in word_letters list
                if user_input in word_letters:
                    window["-OUT-"].update("Zgadłeś literę. Brawo")

                    # find indexes of correctly guessed letter
                    for i, letter in enumerate(word_letters):
                        # and replace blanks with letters
                        if word_letters[i] == user_input:
                            word_blanks[i] = word[i]
                    # output updated word
                    window["-WORD-"].update("".join(word_blanks), font="Young 24")

                    # win condition
                    if "".join(word_blanks) == "".join(word_letters):
                        window["-OUT-"].update("Wygrałeś! Brawo!")
                        points += 1
                        window["-POINTS-"].update(str(points))
                        sg.popup("Wygrana, losuję nowe słowo", font=font_used)
                        hangman()
                # lost condition
                else:
                    lives = lives - 1
                    window["-OUT-"].update("Pudło, spróbuj jeszcze raz")
                    window["-HANGMAN-"].update(hangman_art[lives])
                    window["-LIVES-"].update(lives)
                    window["-WORD-"].update("".join(word_blanks), font="Young 24")
                    if lives == 0:
                        window["-OUT-"].update("Przegrałeś!")
                        sg.popup(f"Przegrana. Losuję nowe słowo, słowo to: {word}", font=font_used)
                        hangman()
            # output if letter already been chosen
            else:
                window["-OUT-"].update("Ta litera już była.")

    window.close()


if __name__ == '__main__':
    hangman()
