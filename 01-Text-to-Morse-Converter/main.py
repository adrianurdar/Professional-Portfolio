# Text to Morse Code Converter

MORSE_CODE_DICT = {
    'A': '·-',
    'B': '-···',
    'C': '-·-·',
    'D': '-··',
    'E': '·',
    'F': '··-·',
    'G': '--·',
    'H': '····',
    'I': '··',
    'J': '·---',
    'K': '-·-',
    'L': '·-··',
    'M': '--',
    'N': '-·',
    'O': '---',
    'P': '·--·',
    'Q': '--·-',
    'R': '·-·',
    'S': '···',
    'T': '-',
    'U': '··-',
    'V': '···-',
    'W': '·--',
    'X': '-··-',
    'Y': '-·--',
    'Z': '--··',
    '1': '·----',
    '2': '··---',
    '3': '···--',
    '4': '····-',
    '5': '·····',
    '6': '-····',
    '7': '--···',
    '8': '---··',
    '9': '----·',
    '0': '-----',
    ',': '--··--',
    '.': '·-·-·-',
    '?': '··--··',
    '/': '-··-·',
    '-': '-····-',
    '(': '-·--·',
    ')': '-·--·-',
    ' ': '       '
}

input_ok = False

while not input_ok:
    # User inputs a string
    user_input = input("What message you want to convert to Morse Code?\n"
                       "You can use all letter from A to Z, and the symbols: ,.?/-()\n")
    modified_user_input = user_input.upper()

    # Escape special characters
    for letter in modified_user_input:
        if letter not in MORSE_CODE_DICT.keys():
            print(f"You cannot use '{letter}' in your message.")
            input_ok = False
            break
        input_ok = True

# Convert the string into morse code
converted_list = [MORSE_CODE_DICT[letter] for letter in modified_user_input]

print(f"Your message ({user_input}) converted to Morse Code: {'   '.join(converted_list)}")
