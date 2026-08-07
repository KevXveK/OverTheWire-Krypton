import sys
import string

list_alphabet = string.ascii_uppercase
filename = sys.argv[1]
with open(filename, 'r', encoding = 'utf-8') as file:
    file_contents = file.read()
phrase_decoded = []
attempt  = 0
def ceaser_decode(file_contents):
    shift_number = 0
    while len(phrase_decoded) < 26:
        shifted_text = list_alphabet[shift_number:] + list_alphabet[:shift_number]
        map_table = str.maketrans(list_alphabet, shifted_text)
        phrase_decoded.append(file_contents.translate(map_table))
        shift_number += 1
    return phrase_decoded
test_decoded = ceaser_decode(file_contents)
while attempt < 26:
    print(f"Cipher number {attempt}: {test_decoded[attempt]} \n")
    attempt += 1
