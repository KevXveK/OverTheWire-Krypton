import string

list_alphabet = string.ascii_uppercase
text_value = input("Type your text: ").upper()
phrase_decoded = []
attempt  = 0
def ceaser_decode(text):
    shift_number = 0
    while len(phrase_decoded) < 26:
        shifted_text = list_alphabet[shift_number:] + list_alphabet[:shift_number]
        map_table = str.maketrans(list_alphabet, shifted_text)
        phrase_decoded.append(text.translate(map_table))
        shift_number += 1
    return phrase_decoded
test_decoded = ceaser_decode(text_value)
while attempt < 26:
    print(f"Cipher number {attempt}: {test_decoded[attempt]} \n")
    attempt += 1
