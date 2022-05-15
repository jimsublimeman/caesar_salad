# set alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# define functions
def encrypt(plain_text, shift_number):
    ciphered_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_number
            ciphered_text += alphabet[new_position]
        else:
            ciphered_text += letter
    print(f"Your encrypted message is {ciphered_text}")

def decrypt(scrambled_text, shift_number):
    deciphered_text =""
    for letter in scrambled_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - shift_number
            deciphered_text += alphabet[new_position]
        else:
            deciphered_text += letter
    print(f"Your decrypted message is {deciphered_text}")

# create direction and inputs
from art import new_logo
print("Welcome to the Caesar Cipher Program!")
print(new_logo)

#Start a while loop here 
# call the right arguments to pass back into encrypt or decrypt and fix modulo shit
program_running = True

while program_running:
    direction = input("Type 'encode' to encrypt your message or 'decode' to decrypt:\n")
    text = input("Type your message here:\n").lower()
    shift = int(input("State the number of characters to shift by:\n"))
    shift = shift % len(alphabet)

    if direction == "encode": 
        encrypt(plain_text = text, shift_number = shift)
    elif direction == "decode":
        decrypt(scrambled_text = text, shift_number = shift)
    else:
        print("Sorry, please type 'encode' or 'decode' to use the cipher.")
    user_input = input('To continue, press any key. To exit, press "e". ')
    if user_input == 'e':
        program_running = False
