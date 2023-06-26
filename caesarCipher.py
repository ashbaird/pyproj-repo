from operator import index


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    arr_text = []
    for letter in text:
        x = alphabet.index(letter)
        new_index = (x + shift) % 26
        arr_text.append(alphabet[new_index])
        str_text = "".join(arr_text)
    return str_text      

def decrypt(text, shift):
    arr_text = []
    for letter in text:
        x = alphabet.index(letter)
        new_index = (x - shift) % 26
        arr_text.append(alphabet[new_index])
        str_text = "".join(arr_text)
    return str_text    

if direction == "encode":
    encryptedResult = encrypt(text, shift)
    print(f"The encoded text is {encryptedResult}")
if direction == 'decode':
    decryptedResult = decrypt(text, shift)
    print(f"The decoded text is {decryptedResult}")
