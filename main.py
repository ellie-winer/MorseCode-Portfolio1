import os
from time import sleep


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',', '?', '\'', '!', '/', '(', ')', '&', ':', ';', '=', '+', '-', '_', '"', '$', '@']
morse_alphabet = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...','-','..-','...-','.--','-..-','-.--','--..', '.---', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----', '.-.-.-', '--..--', '..--..', '# .----.', '-.-.--', '-..-.', '-.--.', '-.--.-', '.-...', '---...', '-.-.-.', '-...-', '.-.-.', '-....-', '..--.-', '.-..-.', '...-..-', '.--.-.']



morse_dict = dict(zip(alphabet, morse_alphabet))


def morse_code(start_text):
    coded_word = ""
    for char in start_text:
        if char == '~':
            coded_word += ' / '
        else:
            if char in alphabet:
                coded_letter = morse_dict.get(char)
                coded_word += coded_letter
                coded_word += " "
    print(f"Here is your word in morse code: {coded_word}")
                
should_continue = True
while should_continue:
    os.system('clear')
    print('Morse Machine On')
    sleep(1)
    text = input(f'\nWhat do you want to convert to morse code?:\n').lower()
    fixed_text = text.replace(' ', '~')

    morse_code(start_text=fixed_text)

    continue_code = input('\nType "yes" to go again. Type "no" to stop:\n')
    if continue_code == 'no':
        should_continue = False
        print("Morse Code Machine off")