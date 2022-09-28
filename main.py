
# Prompt : A text-based Python program to convert Strings into Morse Code.

import pandas as pd

data = pd.read_csv(r'C:\Users\wcogh\PycharmProjects\Portfolio Projects\MorseCodeGuide.csv', encoding='unicode_escape')
morse_code = {data['LETTER'][num] : data['MORSECODE'][num] for num in range(len(data))}

# # or if the csv file isnt available....
# morse_code = {
# 'A' : '.-','B' : '-...','C' : '-.-.','D' : '-..','E' : '.','F' : '..-.','G' : '--.','H' : '....','I' : '..','J' : '.---',
# 'K' : '-.-','L' : '.-..','M' : '--','N' : '-.','O' : '---','P' : '.--.','Q' : '--.-','R' : '.-.','S' : '...','T' : '-',
# 'U' : '..-','V' : '...-','W' : '.--','X' : '-..-','Y' : '-.--','Z' : '--..','0' : '-----','1' : '.----','2' : '..---',
# '3' : '...--','4' : '....-','5' : '.....','6' : '-....','7' : '--...','8' : '---..','9' : '----.','.' : '.-.-.-','(' : '-.--.',
# '+' : '.-.-.','¿' : '..-.-',',' : '--..--',')' : '-.--.-','-' : '-....-','¡' : '--...-','?' : '..--..','&' : '.-...','_' : '..--.-',
# "'" : '.----.',':' : '---...','"' : '.-..-.','!' : '-.-.--',';' : '-.-.-.','$' : '...-..-','/' : '-..-.','=' : '-...-','@' : '.--.-.', ' ': '/'}

def string_to_morse():
    # Step 1 : Take a String input.
    string_input = input(f'Please insert a string here \n').upper()

    # Step 2 : Convert the String into Morse Code.
    translated_input = [morse_code[string_input[num]] if morse_code[string_input[num]] != ' ' else ' ' for num in range (len(string_input))]

    # Step 3 : Provide the Morse Code.
    final_output = ' '.join(translated_input)
    print(final_output)

# # AND THE REVERSE

def morse_to_string():
    # Step 1 : Take a morse code input.
    morse_input = input(f'Please insert a morse code here \n')

    #Step 1a : Seperate the characters into words by looking at the spaces
    to_translate = morse_input.split()

    #step 1b : Convert the / between the words into a different character, as if we dont translate a / could be read
    #as part of the message when it really isnt, so convert to a tilde which doesnt have a morse translation.
    for x in range(len(to_translate)):
        if to_translate[x] == '/':
            to_translate[x] = '~'


    # Step 2 : Convert the Morse Code into string.

    translation = [ list(morse_code.keys())[list(morse_code.values()).index(to_translate[x])]
                    if to_translate[x] != '~' else ' ' for x in range(len(to_translate)) ]




    # Step 3 : Provide the string.

    final_translation = ''.join(translation)
    print(final_translation)
answer = input('What would you like to do? \n'
               'Type T to convert a text string to morse code, or M to decode a Morse Code message. \n') .upper()

if answer == 'M':
    morse_to_string()
elif answer == 'T':
    string_to_morse()
else:
    print('You have not made a valid selection.')